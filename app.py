import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from logic_engine import predict_metrics  # <--- NEW IMPORT
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
    /* Force Metrics to look professional */
    div[data-testid="stMetricValue"] {
        font-size: 28px !important;
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
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)
# --- SIDEBAR CONTROLS ---
st.sidebar.markdown("## 📡 CONTROL TOWER")
st.sidebar.divider()
# 1. NEW: Month Selector
selected_month = st.sidebar.selectbox("🗓️ Select Month", 
    ["January", "February", "March", "April", "May", "June", 
     "July", "August", "September", "October", "November", "December"])
# 2. Day & Time
selected_day = st.sidebar.selectbox("📅 Day of Week", 
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
selected_hour = st.sidebar.slider("⏰ Time of Day (24h)", 0, 23, 18)
st.sidebar.markdown("### ⛈️ SCENARIO PLANNING")
# Auto-suggest weather based on month
default_weather = "Snowstorm" if selected_month in ["January", "February"] else "Clear"
weather = st.sidebar.radio("Weather Condition", ["Clear", "Rain", "Snowstorm"], index=0 if default_weather == "Clear" else 2, horizontal=True)
surge_multiplier = st.sidebar.slider("⚡ Surge Pricing (x)", 1.0, 3.5, 1.5)
# --- LOGIC ENGINE CALL ---
# Now we just call the imported function instead of defining it here
demand, revenue, profit = predict_metrics(selected_month, selected_day, selected_hour, surge_multiplier, weather)
# --- HEADER ---
c1, c2 = st.columns([1, 8])
with c1: st.markdown("# ⚡")
with c2: 
    st.title("CYBERCAB OPERATIONS CENTER")
    st.markdown(f"### 🗓️ Period: {selected_month} 2026 | 🤖 Fleet Status: ONLINE")
st.divider()
# --- TOP METRICS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("📍 Active Requests", f"{demand}", f"{'+' if weather != 'Clear' else ''}{int(demand*0.05)} vs Forecast")
m2.metric("💰 Gross Revenue (Hr)", f"${revenue:,.0f}", "Live Actuals")
m3.metric("📉 Net Profit", f"${profit:,.0f}", f"{int((profit/revenue)*100)}% Margin")
m4.metric("🔋 Fleet Utilization", f"{min(98, int(demand/8))} %", "Optimal")
# --- ROW 2: MAP & CHARTS ---
st.markdown("---")
col_map, col_chart = st.columns([5, 3])
with col_map:
    st.markdown(f"### 🗺️ Live Fleet Distribution ({selected_month})")
    # Map Logic - Uses Streamlit's built-in map (Safe & Fast)
    lat_center, lon_center = 40.758896, -73.985130 
    map_data = pd.DataFrame(
        np.random.randn(demand, 2) / [50, 50] + [lat_center, lon_center],
        columns=['lat', 'lon']
    )
    st.map(map_data, zoom=11, color='#00A8E8')
with col_chart:
    st.markdown("### 📈 Monthly Seasonal Trend")
    # Show trend across the WHOLE YEAR
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    full_month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # Quick simulation for graph
    monthly_data = [predict_metrics(m, "Wednesday", 17, 1.5, "Clear")[2] for m in full_month_names]
    chart_df = pd.DataFrame({'Month': months, 'Net Profit': monthly_data})
    # Highlight current month
    c = alt.Chart(chart_df).mark_bar(color='#1F2937').encode(
        x=alt.X('Month', sort=None),
        y='Net Profit'
    ).properties(height=350)
    # The active bar is Green
    highlight = alt.Chart(chart_df[chart_df['Month'] == selected_month[:3]]).mark_bar(color='#10B981').encode(
        x=alt.X('Month', sort=None),
        y='Net Profit'
    )
    st.altair_chart(c + highlight, use_container_width=True)
# --- ALERTS ---
if selected_month == "August" and demand < 500:
    st.info("📉 SEASONAL ALERT: 'Summer Dip' detected. Re-routing excess fleet to JFK Airport.")
elif weather == "Snowstorm":
    st.warning("❄️ WINTER PROTOCOL: Maximize regenerative braking. Deploy AWD units only.")
else:
    st.success("✅ SYSTEM OPTIMAL: Standard patrol routes active.")