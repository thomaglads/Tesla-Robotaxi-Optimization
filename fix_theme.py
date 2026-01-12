import os

# 1. ENSURE CONFIG IS PERFECT
config_dir = ".streamlit"
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

config_content = """
[theme]
base = "dark"
primaryColor = "#00A8E8"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#1F2937"
textColor = "#FAFAFA"
font = "sans serif"
"""

with open(f"{config_dir}/config.toml", "w") as f:
    f.write(config_content)

# 2. WRITE THE "GOD TIER" APP
app_code = r'''
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="CyberCab Operations Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING ---
st.markdown("""
<style>
    /* METRICS */
    div[data-testid="stMetricValue"] {
        font-size: 32px !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #9CA3AF !important; 
        text-transform: uppercase;
    }
    div[data-testid="stMetric"] {
        background-color: #1F2937;
        border: 1px solid #374151;
        padding: 15px;
        border-radius: 10px;
    }
    /* HEADERS */
    h1 { color: #FFFFFF !important; font-weight: 900 !important; letter-spacing: -1px; }
    h2, h3 { color: #E5E7EB !important; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
st.sidebar.markdown("## 📡 CONTROL TOWER")
st.sidebar.divider()

# 1. Time Controls
selected_day = st.sidebar.selectbox("📅 Operational Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
selected_hour = st.sidebar.slider("⏰ Time of Day (24h)", 0, 23, 18)

# 2. Scenario Controls
st.sidebar.markdown("### ⛈️ SCENARIO PLANNING")
weather = st.sidebar.radio("Weather Condition", ["Clear", "Rain", "Snowstorm"], horizontal=True)
surge_multiplier = st.sidebar.slider("⚡ Surge Pricing (x)", 1.0, 3.5, 1.5 if weather == "Clear" else 2.5)

# --- LOGIC ENGINE ---
def predict_metrics(day, hour, surge, weather_cond):
    base_demand = 400
    
    # Time Logic
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        if 7 <= hour <= 10: base_demand += 300 # AM Rush
        if 16 <= hour <= 19: base_demand += 450 # PM Rush
    if day in ["Friday", "Saturday"] and hour >= 20: base_demand += 400 # Nightlife
    
    # Weather Logic
    if weather_cond == "Rain": base_demand *= 1.3
    if weather_cond == "Snowstorm": base_demand *= 0.8 # Fewer riders, but higher surge
    
    # Price Elasticity (Higher price = slightly lower demand)
    elasticity = 1.0 - (surge * 0.1) 
    final_demand = int(base_demand * elasticity)
    
    # Financials
    gross_revenue = final_demand * (22 * surge)
    op_cost = final_demand * 4.50 # Charging + Maintenance per ride
    net_profit = gross_revenue - op_cost
    
    return final_demand, gross_revenue, net_profit

# Calculate Current State
demand, revenue, profit = predict_metrics(selected_day, selected_hour, surge_multiplier, weather)

# --- MAIN DASHBOARD LAYOUT ---

# Header
c1, c2 = st.columns([1, 8])
with c1: st.markdown("# ⚡")
with c2: 
    st.title("CYBERCAB OPERATIONS CENTER: NYC")
    st.markdown("### 🤖 Autonomous Fleet Dispatch & Profit Optimization")

st.divider()

# Top Level Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("📍 Active Requests", f"{demand}", f"{'+' if weather != 'Clear' else ''}{int(demand*0.05)} vs Forecast")
m2.metric("💰 Gross Revenue (Hr)", f"${revenue:,.0f}", "Live Actuals")
m3.metric("📉 Net Profit", f"${profit:,.0f}", f"{int((profit/revenue)*100)}% Margin")
m4.metric("🔋 Fleet Utilization", f"{min(98, int(demand/8))} %", "Optimal")

# --- ROW 2: MAP & CHARTS ---
st.markdown("---")
col_map, col_chart = st.columns([5, 3])

with col_map:
    st.markdown("### 🗺️ Live Demand Heatmap (Manhattan Sector)")
    
    # Generate Mock Geospatial Data centered on NYC
    lat_center, lon_center = 40.758896, -73.985130 # Times Square
    
    # Create random points around NYC based on demand
    df_map = pd.DataFrame(
        np.random.randn(demand, 2) / [50, 50] + [lat_center, lon_center],
        columns=['lat', 'lon']
    )

    # 3D Hexagon Layer
    layer = pdk.Layer(
        "HexagonLayer",
        df_map,
        get_position='[lon, lat]',
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,
        coverage=1,
    )

    # Render Map
    view_state = pdk.ViewState(
        latitude=lat_center,
        longitude=lon_center,
        zoom=11,
        pitch=50,
    )
    
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Demand Cluster"},
        map_style="mapbox://styles/mapbox/dark-v10" # Dark mode map
    ))

with col_chart:
    st.markdown("### 📈 24h Trend")
    hours = list(range(24))
    # Generate trend line
    trend_data = [predict_metrics(selected_day, h, surge_multiplier, weather)[0] for h in hours]
    chart_df = pd.DataFrame({'Hour': hours, 'Demand': trend_data})
    
    # Green Profit Line
    c = alt.Chart(chart_df).mark_area(
        line={'color':'#10B981'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='#10B981', offset=0),
                   alt.GradientStop(color='rgba(16, 185, 129, 0.1)', offset=1)]
        )
    ).encode(
        x='Hour', 
        y='Demand'
    ).properties(height=350)
    
    st.altair_chart(c, use_container_width=True)

# --- ALERT SYSTEM ---
if weather == "Snowstorm":
    st.warning("❄️ WINTER PROTOCOL: Maximize regenerative braking. Deploy AWD units only.")
elif profit > 15000:
    st.success("🚀 SURGE OPTIMIZED: Revenue target exceeded. Hold current pricing.")
else:
    st.info("📡 STANDARD OPS: Monitoring fleet distribution.")
'''

# Write the file
with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code)

print("✅ SUCCESS: CyberCab Dashboard with 3D MAPS is ready!")