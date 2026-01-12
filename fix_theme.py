import os

# 1. CREATE THE CONFIG FILE (Forces Dark Mode & Tesla Red)
config_dir = ".streamlit"
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

config_content = """
[theme]
base = "dark"
primaryColor = "#e82127"
backgroundColor = "#000000"
secondaryBackgroundColor = "#1c1c1c"
textColor = "#ffffff"
font = "sans serif"
"""

with open(f"{config_dir}/config.toml", "w") as f:
    f.write(config_content)
    print("✅ Configured Streamlit for Dark Mode.")

# 2. WRITE THE APP FILE (Professional Fonts & Layout)
app_code = r'''
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Tesla Fleet Command",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING (THE "PRO" LOOK) ---
st.markdown("""
<style>
    /* 1. METRIC VALUES (The Big Numbers) */
    div[data-testid="stMetricValue"] {
        font-size: 46px !important;
        font-weight: 900 !important;
        color: #FFFFFF !important;
        text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
    }
    
    /* 2. METRIC LABELS (The Small Titles) */
    div[data-testid="stMetricLabel"] {
        font-size: 16px !important;
        font-weight: 700 !important;
        color: #e82127 !important; /* Tesla Red */
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* 3. METRIC CARDS (Background) */
    div[data-testid="stMetric"] {
        background-color: #111111;
        border: 1px solid #333;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
    }

    /* 4. HEADERS */
    h1 {
        font-weight: 800 !important;
        color: #e82127 !important;
        text-transform: uppercase;
    }
    h3 {
        color: #cccccc !important;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([1, 6])
with col1:
    # Tesla Logo Placeholder
    st.markdown("## ⚡")
with col2:
    st.title("Tesla Fleet Command")
    st.markdown("### 📡 Live Dispatch & Optimization System")

st.divider()

# --- SIDEBAR ---
st.sidebar.markdown("### 🕹️ OPERATIONS CENTER")
st.sidebar.divider()
selected_day = st.sidebar.selectbox("📅 Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
selected_hour = st.sidebar.slider("⏰ Dispatch Hour", 0, 23, 17)
surge_multiplier = st.sidebar.slider("⚡ Surge Multiplier", 1.0, 3.0, 1.5)

# --- LOGIC ---
def predict_demand(day, hour, surge):
    base = 400
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        if 7 <= hour <= 10: base += 300
        if 16 <= hour <= 19: base += 450
    if day in ["Friday", "Saturday"] and hour >= 20: base += 400
    
    final_demand = base * (1 / (surge * 0.8))
    return int(final_demand + np.random.randint(-20, 20))

trips = predict_demand(selected_day, selected_hour, surge_multiplier)
revenue = trips * (25 * surge_multiplier)
fleet_needed = int(trips * 1.1)

# --- METRICS ROW ---
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("📍 Predicted Demand", f"{trips}", f"{int(trips*0.12)} vs Avg")
with c2:
    st.metric("💰 Hourly Revenue", f"${revenue:,.0f}", "High Yield")
with c3:
    st.metric("🚖 Fleet Required", f"{fleet_needed}", "Active Units")

# --- CHART AREA ---
st.markdown("---")
st.markdown(f"### 📉 24-Hour Demand Forecast: {selected_day}")

hours = list(range(24))
demands = [predict_demand(selected_day, h, surge_multiplier) for h in hours]
chart_data = pd.DataFrame({'Hour': hours, 'Demand': demands})

# Tesla Red Area Chart
chart = alt.Chart(chart_data).mark_area(
    line={'color':'#e82127'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='#e82127', offset=0),
               alt.GradientStop(color='rgba(232, 33, 39, 0.1)', offset=1)]
    )
).encode(
    x=alt.X('Hour', title='Time of Day'),
    y=alt.Y('Demand', title='Trip Count'),
    tooltip=['Hour', 'Demand']
).properties(height=400)

st.altair_chart(chart, use_container_width=True)

# --- STRATEGY ALERT ---
if trips > 500:
    st.error("🚨 HIGH DEMAND ALERT: Deploy Reserves from Queens Depot.")
elif trips < 150:
    st.info("🔋 CHARGING MODE: Route excess units to Supercharger Hubs.")
else:
    st.success("✅ OPTIMAL STATE: Maintain patrol routes.")
'''

with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code)
    print("✅ App rebuilt with Professional Tesla Styles.")