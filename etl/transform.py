import pandas as pd
from datetime import datetime

def transform_weather_data(raw_data):
    """
    Transforms raw JSON weather data into a clean pandas DataFrame.
    """
    if not raw_data or "main" not in raw_data:
        return None

    try:
        # Extracting relevant information
        transformed_data = {
            "City": raw_data.get("name"),
            "Country": raw_data.get("sys", {}).get("country"),
            "Temperature (°C)": raw_data.get("main", {}).get("temp"),
            "Feels Like (°C)": raw_data.get("main", {}).get("feels_like"),
            "Humidity (%)": raw_data.get("main", {}).get("humidity"),
            "Pressure (hPa)": raw_data.get("main", {}).get("pressure"),
            "Wind Speed (m/s)": raw_data.get("wind", {}).get("speed"),
            "Weather": raw_data.get("weather", [{}])[0].get("description"),
            "Timestamp": datetime.fromtimestamp(raw_data.get("dt")).strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Convert to DataFrame
        df = pd.DataFrame([transformed_data])
        return df
    except Exception as e:
        print(f"Error during transformation: {e}")
        return None
