# 🌤️ Weather Pulse: Dynamic ETL & Analytics Dashboard

**Weather Pulse** is a professional-grade weather monitoring system that combines a modular **ETL (Extract, Transform, Load)** pipeline with a premium **Streamlit** dashboard. It fetches real-time data, processes it into structured formats, and provides smart insights and visualizations.

---

## ✨ Key Features

### 🔄 1. Dynamic ETL Pipeline
*   **Extract:** Fetches real-time weather data from the OpenWeatherMap API with built-in response caching to optimize performance.
*   **Transform:** Cleans and structures raw JSON data into a professional Dataframe format using `pandas`, handling multi-city trends.
*   **Load:** Automatically maintains a local CSV history (`weather_history.csv`) for persistent tracking.

### 🎨 2. Premium UI/UX Design
*   **Soft Blue Theme:** A tailored, professional aesthetic with a sky-blue gradient and clean typography.
*   **Glassmorphism:** Elegant, semi-transparent cards with hover animations for a modern feel.
*   **Custom Fonts:** Integrated **'Outfit'** font from Google Fonts for a sleek look.

### 💡 3. Smart Features
*   **City Autocorrect:** Uses `fuzzywuzzy` algorithms to detect and correct misspelled city names (e.g., "Krachi" → "Karachi").
*   **Contextual Insights:** A smart card that provides weather-based advice (e.g., "It's raining! Keep an umbrella handy ☔").
*   **Location Awareness:** Special tips for unique locations like Antarctica.

### 📊 4. Interactive Analytics
*   **Trend Tracking:** Real-time Plotly charts for Temperature and Humidity trends over time.
*   **Historical View:** An expandable records section for detailed data auditing.

---

## 🛠️ Project Structure

```text
dynamic_etl_project/
├── api_client/        # API communication & Caching
├── etl/               # ETL Pipeline (Extract, Transform, Load)
├── dashboard/         # Logic for interactive Plotly charts
├── utils/             # Configuration & Constants
├── cache/             # Temporary storage for API responses
├── app.py             # Main Entry Point (Streamlit Dashboard)
├── requirements.txt   # Project Dependencies
└── weather_history.csv # Historical weather database
```

---

## 🚀 How to Run

### 1. Prerequisites
Make sure you have Python 3.9+ installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup API Key
Go to `api_client/weather_api.py` (or your config file) and ensure your OpenWeatherMap API key is active.

### 4. Launch the Dashboard
```bash
streamlit run app.py
```

---

## 🔧 Technologies Used
*   **Frontend:** Streamlit, Custom CSS/HTML
*   **Data Processing:** Pandas, NumPy
*   **Visualization:** Plotly Express
*   **API Client:** Requests, FuzzyWuzzy
*   **Data Storage:** CSV (Exportable/Portable)

---
*Created with ❤️ for a professional weather analytics experience.*
