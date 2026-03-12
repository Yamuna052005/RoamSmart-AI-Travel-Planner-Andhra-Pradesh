from fastapi import FastAPI, Query, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from database_loader import load_data
from ml_models.cost_predictor import train_cost_model, predict_cost
from services.weather_services import get_weather
from ml_models.recommender import collaborative_recommendations
from ai.itinerary import router as itinerary_router  # include itinerary routes

app = FastAPI(title="RoamSmart AI Travel Planner For Andhra Pradesh")

# -----------------------------
# CORS Middleware
# -----------------------------
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Pydantic Models
# -----------------------------
class Destination(BaseModel):
    name: str
    latitude: float
    longitude: float

class AssistantRequest(BaseModel):
    query: str

class RecommendationRequest(BaseModel):
    location: str
    category: str
    season: str
    duration: int

# -----------------------------
# Startup Event (Load Resources)
# -----------------------------
@app.on_event("startup")
def startup():
    destinations, ratings = load_data()
    # Remove duplicates by name at startup
    destinations = destinations.drop_duplicates(subset=["name"]).reset_index(drop=True)
    app.state.destinations = destinations
    app.state.ratings = ratings
    app.state.cost_model = train_cost_model(destinations.to_dict(orient="records"))

# -----------------------------
# Home Route
# -----------------------------
@app.get("/")
def home():
    return {"message": "RoamSmart Backend Running Successfully"}

# -----------------------------
# Cost Prediction API
# -----------------------------
@app.get("/predict_cost")
def cost(rating: float, category: str, city: str, distance: float, season: str):
    price = predict_cost(
        app.state.cost_model,
        rating,
        category,
        city,
        distance,
        season
    )
    return {"predicted_cost": price}

# -----------------------------
# Weather API
# -----------------------------
@app.get("/weather")
def weather(city: str = Query(..., description="City name")):
    return get_weather(city)

# -----------------------------
# Day-by-Day Itinerary + Route Optimization
# -----------------------------
app.include_router(itinerary_router)

# -----------------------------
# Get All Destinations (Map)
# -----------------------------
@app.get("/destinations")
def get_destinations():
    unique_destinations = app.state.destinations.drop_duplicates(subset=["name"])
    unique_destinations = unique_destinations.drop(columns=["image_url"], errors="ignore")
    return unique_destinations.to_dict(orient="records")

# -----------------------------
# Recommendations API
# -----------------------------
recommend_router = APIRouter(prefix="/recommend", tags=["Recommendations"])

@recommend_router.post("/")
def recommend(user_id: int):
    return collaborative_recommendations(
        user_id,
        app.state.destinations,
        app.state.ratings
    )

@app.post("/recommendations")
def get_recommendations(req: RecommendationRequest):
    destinations = app.state.destinations

    location = req.location.strip().lower()
    category = req.category.strip().lower()
    season = req.season.strip().lower()
    duration = max(1, req.duration)

    # Filter by location and category
    filtered = destinations[
        (destinations["city"].str.lower() == location) &
        (destinations["category"].str.lower() == category)
    ].drop_duplicates(subset=["name"])

    # Include places that match the season OR are 'all'
    filtered = filtered[
        filtered["season"].str.lower().isin([season, "all"])
    ]

    if filtered.empty:
        return {"message": f"No {req.category} places found in {req.location} for {req.season} season."}

    # Split for multi-day itinerary
    per_day_count = max(1, len(filtered) // duration)
    itinerary = [
        filtered.iloc[i*per_day_count:(i+1)*per_day_count].drop(columns=["image_url"], errors="ignore").to_dict(orient="records")
        for i in range(duration)
    ]

    # Add remaining places
    remaining = filtered.iloc[duration*per_day_count:].drop(columns=["image_url"], errors="ignore").to_dict(orient="records")
    for idx, place in enumerate(remaining):
        itinerary[idx % duration].append(place)

    return {"itinerary": itinerary}

# -----------------------------
# AI Assistant API
# -----------------------------
@app.post("/assistant")
def assistant(request: AssistantRequest):
    query = request.query.lower()

    if "weather" in query:
        return {"reply": "Sure! Use the Weather section to check live conditions for any city."}
    elif "tirupati" in query and "temple" in query:
        return {"reply": "Tirupati is famous for Sri Venkateswara Temple and other sacred places."}
    elif "plan" in query or "itinerary" in query:
        return {"reply": "I can generate a day‑by‑day itinerary for your trip."}
    elif "cost" in query or "budget" in query:
        return {"reply": "I can estimate travel costs for destinations using the Cost Predictor."}
    else:
        return {"reply": f"You asked: {request.query}. I’ll help you explore Andhra Pradesh!"}