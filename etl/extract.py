def extract_weather_data(city: str):
    """
    Extracts weather data for a given city using the weather_api client.
    """
    from api_client.weather_api import fetch_weather, autocorrect_city
    
    corrected_city = autocorrect_city(city)
    found_autocorrect = (corrected_city.lower() != city.lower())
    
    print(f"Extracting data for: {corrected_city}...")
    data = fetch_weather(corrected_city)
    
    if not data or "error" in data:
        error_msg = data.get("error") if data else "Unknown error"
        return {"success": False, "error": error_msg}
        
    return {
        "success": True, 
        "data": data, 
        "corrected_name": corrected_city if found_autocorrect else None
    }
