import requests

API_KEY = "82a0d03bc8a82eaae1904a8cdf2ea2dd"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):

    try:

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}