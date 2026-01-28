import os
import pandas as pd

DATA_FILE = "weather_history.csv"

def load_weather_data(df: pd.DataFrame):
    """
    Loads/Appends the transformed DataFrame into a CSV file for history.
    """
    if df is None or df.empty:
        return False
    
    try:
        # If file doesn't exist, create it with header, else append without header
        if not os.path.exists(DATA_FILE):
            df.to_csv(DATA_FILE, index=False)
        else:
            df.to_csv(DATA_FILE, mode='a', header=False, index=False)
        
        print(f"Data successfully loaded to {DATA_FILE}")
        return True
    except Exception as e:
        print(f"Error during loading: {e}")
        return False
