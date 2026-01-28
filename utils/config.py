import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file (for local)
load_dotenv()

# Priority: Streamlit Secrets > Environment Variables
if "OPENWEATHER_API_KEY" in st.secrets:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
else:
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
