import requests
import json
import os
from utils.config import API_KEY, BASE_URL
from fuzzywuzzy import process

# List of popular cities for autocorrect (can be expanded)
POPULAR_CITIES = [
    "Karachi", "Lahore", "Islamabad", "Faisalabad", "Rawalpindi", "Multan", "Peshawar", "Quetta",
    "London", "New York", "Tokyo", "Paris", "Berlin", "Dubai", "Singapore", "Sydney", "Mumbai",
    "Delhi", "Vostok", "McMurdo", "Antarctica", "Antartica", "Cairo", "Moscow", "Toronto", "Beijing"
]

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def autocorrect_city(city_name: str):
    """
    Suggests the closest matching city name if a misspelling is detected.
    """
    match, score = process.extractOne(city_name, POPULAR_CITIES)
    if score > 80: # If match is strong, return the corrected name
        return match
    return city_name

def fetch_weather(city: str):
    cache_file = os.path.join(CACHE_DIR, f"{city.lower()}.json")

    # 👉 Cache check
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return json.load(f)

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        if response.status_code != 200:
            return {"error": response.json().get("message", "Unknown error")}
        
        data = response.json()
        # 👉 save to cache
        with open(cache_file, "w") as f:
            json.dump(data, f)
        return data
    except Exception as e:
        return {"error": str(e)}
