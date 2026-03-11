import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError, OperationalError

# PostgreSQL connection
engine = create_engine("postgresql://postgres:Palepogu%4019@localhost:5432/roamsmart")

AP_CITIES = {
    "tirupati",
    "visakhapatnam",
    "vijayawada",
    "kadapa",
    "kurnool",
    "anantapur",
    "rajahmundry",
    "guntur",
    "nellore",
    "chittoor",
}

def _load_ratings_table():
    try:
        return pd.read_sql("SELECT * FROM public.user_ratings", engine)
    except (ProgrammingError, OperationalError):
        # Fallback if user_ratings table doesn’t exist
        return pd.read_sql("SELECT * FROM public.ratings", engine)

def load_data():
    destinations = pd.read_sql("SELECT * FROM public.destinations", engine)
    ratings = _load_ratings_table()

    # Normalize city names and filter only AP cities
    if "city" in destinations.columns:
        normalized_city = destinations["city"].astype(str).str.strip().str.lower()
        destinations = destinations[normalized_city.isin(AP_CITIES)].copy()

    # Ensure ratings only include destinations present in destinations table
    if "destination_id" in ratings.columns and "id" in destinations.columns:
        ratings = ratings[ratings["destination_id"].isin(destinations["id"])].copy()

    # ✅ Ensure required columns exist
    required_cols = ["rating", "category", "city", "distance", "season", "estimated_cost"]
    for col in required_cols:
        if col not in destinations.columns:
            if col in ["rating", "estimated_cost", "distance"]:
                destinations[col] = 0
            else:
                destinations[col] = "unknown"

    # ✅ Fill NaN values with safe defaults
    destinations = destinations.fillna({
        "rating": 0,
        "estimated_cost": 0,
        "distance": 0,
        "season": "unknown",
        "category": "unknown",
        "city": "unknown"
    })

    # ✅ Debug logging (optional, helps confirm data loaded)
    print(f"Loaded {len(destinations)} destinations and {len(ratings)} ratings")

    return destinations, ratings
