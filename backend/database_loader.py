import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError, OperationalError

# PostgreSQL connection
engine = create_engine("postgresql://postgres:Palepogu%4019@localhost:5432/roamsmart")

def _load_ratings_table():
    try:
        # Try primary ratings table
        return pd.read_sql("SELECT * FROM public.user_ratings", engine)
    except (ProgrammingError, OperationalError):
        # Fallback if user_ratings table doesn’t exist
        return pd.read_sql("SELECT * FROM public.ratings", engine)

def load_data():
    # Load destinations and ratings
    destinations = pd.read_sql("SELECT * FROM public.destinations", engine)
    ratings = _load_ratings_table()

    # -----------------------------
    # Normalize city names
    # -----------------------------
    if "city" in destinations.columns:
        destinations["city"] = destinations["city"].astype(str).str.strip()

    # -----------------------------
    # Ensure ratings reference valid destinations
    # -----------------------------
    if "destination_id" in ratings.columns and "id" in destinations.columns:
        ratings = ratings[ratings["destination_id"].isin(destinations["id"])].copy()

    # -----------------------------
    # Ensure required ML columns exist
    # -----------------------------
    required_cols = [
        "rating",
        "category",
        "city",
        "distance",
        "season",
        "estimated_cost"
    ]

    for col in required_cols:
        if col not in destinations.columns:
            if col in ["rating", "estimated_cost", "distance"]:
                destinations[col] = 0
            else:
                destinations[col] = "unknown"

    # -----------------------------
    # Fill missing values safely
    # -----------------------------
    destinations = destinations.fillna({
        "rating": 0,
        "estimated_cost": 0,
        "distance": 0,
        "season": "unknown",
        "category": "unknown",
        "city": "unknown"
    })

    # -----------------------------
    # Debug log to verify loading
    # -----------------------------
    print(f"Loaded {len(destinations)} destinations and {len(ratings)} ratings")

    return destinations, ratings