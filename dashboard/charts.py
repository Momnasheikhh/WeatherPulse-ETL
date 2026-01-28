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
        title=f"🌡️ Temperature Trend: {df['City'].iloc[0]}",
        markers=True,
        template="plotly_white",
        line_shape="spline",
        color_discrete_sequence=["#ff6b6b"]
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#1e3a5f", size=14, family="Outfit"),
        title=dict(font=dict(size=20, color="#1e3a5f")),
        margin=dict(t=50, b=50, l=50, r=50)
    )
    fig.update_xaxes(
        showgrid=True, gridwidth=1, gridcolor='rgba(30, 58, 95, 0.1)', 
        tickfont=dict(color="#1e3a5f", size=12),
        title=dict(font=dict(color="#1e3a5f", size=14, family="Outfit"))
    )
    fig.update_yaxes(
        showgrid=True, gridwidth=1, gridcolor='rgba(30, 58, 95, 0.1)', 
        tickfont=dict(color="#1e3a5f", size=12),
        title=dict(font=dict(color="#1e3a5f", size=14, family="Outfit"))
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
        title="💧 Humidity Analysis",
        template="plotly_white",
        color="Humidity (%)",
        color_continuous_scale="Blues"
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#1e3a5f", size=14, family="Outfit"),
        title=dict(font=dict(size=20, color="#1e3a5f")),
        margin=dict(t=50, b=50, l=50, r=50),
        coloraxis_colorbar=dict(
            title=dict(font=dict(color="#1e3a5f", size=12)),
            tickfont=dict(color="#1e3a5f", size=11)
        )
    )
    fig.update_xaxes(
        showgrid=True, gridwidth=1, gridcolor='rgba(30, 58, 95, 0.1)', 
        tickfont=dict(color="#1e3a5f", size=12),
        title=dict(font=dict(color="#1e3a5f", size=14, family="Outfit"))
    )
    fig.update_yaxes(
        showgrid=True, gridwidth=1, gridcolor='rgba(30, 58, 95, 0.1)', 
        tickfont=dict(color="#1e3a5f", size=12),
        title=dict(font=dict(color="#1e3a5f", size=14, family="Outfit"))
    )
    return fig
