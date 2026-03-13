import requests
from requests.exceptions import RequestException, Timeout, HTTPError
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/itinerary", tags=["Itinerary"])

GRAPHOPPER_API_KEY = "Your_API_Key_here"

class RouteRequest(BaseModel):
    places: List[str]

@router.post("/route")
def optimize_route(req: RouteRequest):
    coords = []
    for place in req.places:
        geo_url = f"https://graphhopper.com/api/1/geocode?q={place}&key={GRAPHOPPER_API_KEY}"
        try:
            geo_res = requests.get(geo_url, timeout=10)
            geo_res.raise_for_status()  # raises HTTPError if status != 200
            geo_data = geo_res.json()
        except Timeout:
            return {"message": f"Geocoding request timed out for {place}"}
        except HTTPError as e:
            return {"message": f"Geocoding HTTP error for {place}: {str(e)}"}
        except RequestException as e:
            return {"message": f"Geocoding request failed for {place}: {str(e)}"}

        if geo_data.get("hits"):
            lat = geo_data["hits"][0]["point"]["lat"]
            lon = geo_data["hits"][0]["point"]["lng"]
            coords.append({"name": place, "lat": lat, "lon": lon})
        else:
            return {"message": f"No coordinates found for {place}"}

    if not coords:
        return {"message": "No valid coordinates found for given places."}

    points = "&".join([f"point={c['lat']},{c['lon']}" for c in coords])
    route_url = f"https://graphhopper.com/api/1/route?{points}&vehicle=car&locale=en&key={GRAPHOPPER_API_KEY}"

    try:
        route_res = requests.get(route_url, timeout=20)
        route_res.raise_for_status()
        route_data = route_res.json()
    except Timeout:
        return {"message": "Route request timed out"}
    except HTTPError as e:
        return {"message": f"Route HTTP error: {str(e)}"}
    except RequestException as e:
        return {"message": f"Route request failed: {str(e)}"}

    if "paths" not in route_data or not route_data["paths"]:
        return {"message": "Route could not be generated."}

    path = route_data["paths"][0]

    optimized = [
        {
            "order": idx,
            "name": c["name"],
            "latitude": c["lat"],
            "longitude": c["lon"]
        }
        for idx, c in enumerate(coords, start=1)
    ]

    instructions = [
        {
            "text": inst.get("text"),
            "distance_m": inst.get("distance"),
            "time_ms": inst.get("time")
        }
        for inst in path.get("instructions", [])
    ]

    return {
        "optimized_route": optimized,
        "instructions": instructions,
        "total_distance_km": path["distance"] / 1000,
        "estimated_travel_time_min": path["time"] / 60000
    }

