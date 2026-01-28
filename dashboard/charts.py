import plotly.express as px
import pandas as pd

def create_temperature_chart(df: pd.DataFrame):
    """
    Creates a line chart for temperature trends.
    """
    if df.empty:
        return None
        
    fig = px.line(
        df, 
        x="Timestamp", 
        y="Temperature (°C)", 
        title=f"Temperature Trend: {df['City'].iloc[0]}",
        markers=True,
        template="plotly_white",
        line_shape="spline",
        color_discrete_sequence=["#ff6b6b"] # Soft Red/Orange for Temperature
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#1e3a5f"
    )
    return fig

def create_humidity_chart(df: pd.DataFrame):
    """
    Creates a bar chart for humidity.
    """
    if df.empty:
        return None
        
    fig = px.bar(
        df, 
        x="Timestamp", 
        y="Humidity (%)", 
        title="Humidity Analysis",
        template="plotly_white",
        color="Humidity (%)",
        color_continuous_scale="Blues"
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#1e3a5f"
    )
    return fig
