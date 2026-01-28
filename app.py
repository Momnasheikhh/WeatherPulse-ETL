import streamlit as st
import pandas as pd
import os
from etl.extract import extract_weather_data
from etl.transform import transform_weather_data
from etl.load import load_weather_data
from dashboard.charts import create_temperature_chart, create_humidity_chart

# Page configuration
st.set_page_config(page_title="Weather ETL Dashboard", layout="wide", page_icon="🌦️")

# --- CUSTOM CSS (Soft Blue/Cloudy Theme) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Outfit', sans-serif !important;
    }

    .stApp {
        background: linear-gradient(135deg, #e0f0ff 0%, #c0dfff 100%);
    }

    /* Stylish Heading */
    h1 {
        color: #1e3a5f !important;
        font-weight: 800 !important;
        font-size: 3.8rem !important;
        letter-spacing: -1.5px;
        margin-bottom: 0px !important;
        text-shadow: 2px 2px 0px rgba(255,255,255,0.5); /* Subtle depth */
    }

    h2, h3, .stMarkdown, label {
        color: #1e3a5f !important;
        font-weight: 600;
    }
    
    .stMetric label {
        color: #1e3a5f !important;
        font-size: 1.1rem !important;
        font-weight: 400 !important;
    }

    [data-testid="stMetricValue"] {
        color: #1e3a5f !important;
        font-weight: 800 !important;
        font-size: 2.2rem !important;
    }

    [data-testid="column"] {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px);
        padding: 25px !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        transition: transform 0.3s ease;
    }
    
    [data-testid="column"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05) !important;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.4);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
    }

    .stButton > button {
        background: linear-gradient(90deg, #6ea8fe 0%, #3a6efc 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.7rem 2.5rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(58, 110, 252, 0.3) !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 25px rgba(58, 110, 252, 0.4) !important;
    }

    .insight-card {
        background: rgba(255, 255, 255, 0.9);
        border-left: 10px solid #3a6efc;
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 30px;
        color: #1e3a5f;
        box-shadow: 0 10px 25px rgba(0,0,0,0.02);
    }

    /* Fix for Dark Widgets */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: white !important;
        color: #1e3a5f !important;
        border: 1px solid rgba(0, 0, 0, 0.1) !important;
    }
    
    div[data-testid="stSidebar"] .stSelectbox label, div[data-testid="stSidebar"] .stTextInput label {
        color: #1e3a5f !important;
    }

    input {
        color: #1e3a5f !important;
    }

    /* Expander visibility fix - Normalized */
    [data-testid="stExpander"] summary p, [data-testid="stExpander"] summary svg {
        color: #1e3a5f !important;
        font-weight: 600 !important;
        fill: #1e3a5f !important;
    }
    
    [data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.8) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(30, 58, 95, 0.2) !important;
    }

    /* Dataframe/Table visibility */
    [data-testid="stTable"], [data-testid="stDataFrame"] {
        background-color: white !important;
        border-radius: 10px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 style='text-align: left;'>Weather Pulse ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#5a7a9a; font-size:1.3rem; margin-top:-10px; font-weight:400;'>Real-time analytics with a professional touch.</p>", unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.header("📍 Location Selection")

# Load history to populate dropdown
cities_in_history = []
if os.path.exists("weather_history.csv"):
    df_temp = pd.read_csv("weather_history.csv")
    cities_in_history = df_temp['City'].unique().tolist()

selected_city = st.sidebar.selectbox("Select from history", ["None"] + cities_in_history)
new_city = st.sidebar.text_input("OR Enter New City Name", "")

# Determine which city to use
city = new_city if new_city else selected_city

if st.sidebar.button("Fetch & Process Data"):
    if city and city != "None":
        # ETL Process
        with st.spinner(f"Fetching data for {city}..."):
            result = extract_weather_data(city)
            if result["success"]:
                df = transform_weather_data(result["data"])
                if df is not None:
                    load_weather_data(df)
                    st.session_state["msg"] = f"✅ Data for {df['City'].iloc[0]} updated!"
                    if result.get("corrected_name"):
                        st.session_state["info"] = f"✨ Suggested: **{result['corrected_name']}**"
                    st.rerun()
                else:
                    st.sidebar.error("Transformation failed.")
            else:
                st.sidebar.error(f"Error: {result['error']}")
                if "city not found" in result["error"].lower() or "antarctica" in city.lower():
                    st.sidebar.info("💡 Tip: Try 'Vostok' or 'McMurdo' for Antarctica.")
    else:
        st.sidebar.warning("Please enter or select a city.")

# Display persistent messages
if "msg" in st.session_state:
    st.sidebar.success(st.session_state.pop("msg"))
if "info" in st.session_state:
    st.sidebar.info(st.session_state.pop("info"))

# --- WEATHER INSIGHT LOGIC ---
def get_weather_insight(condition, temp):
    condition = condition.lower()
    insight = "Everything looks normal. Have a great day!"
    
    if "rain" in condition or "drizzle" in condition:
        insight = "It's raining! Keep an umbrella handy. ☔"
    elif "cloud" in condition:
        insight = "It's a bit cloudy. Good for a calm day. ☁️"
    elif "clear" in condition:
        insight = "Clear skies today! Perfect weather for outdoors. ☀️"
        
    if temp >= 35: insight = "It's very hot! Stay hydrated. 🥤"
    elif temp <= 5: insight = "It's quite cold! Wear something warm. 🧥"
    
    return insight

# Main Dashboard
if os.path.exists("weather_history.csv") and city and city != "None":
    df_history = pd.read_csv("weather_history.csv")
    city_df = df_history[df_history['City'].str.lower() == city.lower()]
    
    if not city_df.empty:
        latest = city_df.iloc[-1]
        insight = get_weather_insight(latest['Weather'], latest['Temperature (°C)'])
        
        st.subheader(f"📍 Current Weather in {latest['City']}, {latest['Country']}")
        
        st.markdown(f"""
        <div class="insight-card">
            <h4 style="margin:0;">💡 Smart Insight</h4>
            <p style="margin:5px 0 0 0; font-size:1.1rem;">{insight}</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Temperature", f"{latest['Temperature (°C)']} °C")
        col2.metric("Humidity", f"{latest['Humidity (%)']}%")
        col3.metric("Wind Speed", f"{latest['Wind Speed (m/s)']} m/s")
        col4.metric("Condition", latest['Weather'].capitalize())

        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            temp_fig = create_temperature_chart(city_df)
            if temp_fig: st.plotly_chart(temp_fig, use_container_width=True)
        with c2:
            hum_fig = create_humidity_chart(city_df)
            if hum_fig: st.plotly_chart(hum_fig, use_container_width=True)
        
        with st.expander("View Raw History Data"):
            st.dataframe(city_df.sort_values(by="Timestamp", ascending=False))
    else:
        st.info(f"No history found for {city}. Click 'Fetch & Process Data' to get started.")
else:
    st.info("No data available yet. Please fetch data from the sidebar.")
