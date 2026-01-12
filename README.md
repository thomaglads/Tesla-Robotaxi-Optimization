
 # 🚖 CyberCab Operations Center: NYC Fleet Optimization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tesla-robotaxi-optimization-jltm8e3o25yjo2xysij8fo.streamlit.app/)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Live-success.svg)]()

> **A Next-Gen Dispatch System designed to optimize autonomous fleet profitability by predicting seasonal demand anomalies and weather-driven surges.**

<img width="1897" height="1028" alt="image" src="https://github.com/user-attachments/assets/9cc9599f-0292-4448-ab39-cdf8a0551605" />
https://tesla-robotaxi-optimization-jltm8e3o25yjo2xysij8fo.streamlit.app/

---

## 📌 Executive Summary
**Objective:** Engineer a fleet positioning strategy for a hypothetical Tesla Robotaxi network in NYC.
**Scope:** Analyzed **38 Million** trip records (Jan–Dec 2024) to solve the "Deadhead Mile" profitability crisis.
**Outcome:** Identified **$10M+ in annual efficiency gains** by disproving the "Winter Weather" penalty myth and optimizing summer fleet allocation.

---

## 💰 Business Impact Analysis

| Problem Detected | Data Evidence | Strategic Solution | Est. Value Impact |
| :--- | :--- | :--- | :--- |
| **"The Summer Slump"** | Efficiency ($/Mile) drops **9.6%** in August vs. December. | **Dynamic Cap:** Reduce Midtown fleet by 30% in Q3; redeploy to Airports. | **$4.2M / Year**<br>*(Saved in depreciation)* |
| **"Missing Bankers"** | Midtown Commuter demand collapses **34.8%** in August. | **Shift Strategy:** Move charging windows to 4 PM–6 PM to align with "Nightlife" demand. | **$3.5M / Year**<br>*(Recovered revenue)* |
| **Charging Gaps** | Cars drive ~3.2 miles empty just to charge. | **Gravity Mapping:** Identified 5 optimal zones for vertical charging hubs. | **$2.8M / Year**<br>*(Energy & Time savings)* |
| **Airport Queues** | Drivers wait 60+ mins for $50 fares. | **Arbitrage Algo:** "93-Minute Rule" auto-rejects unprofitable queues. | **+12% Utilization**<br>*(Fleetwide)* |

---

## 📊 Key Findings

### 1. The "Winter Penalty" Myth (Disproven)
* **Hypothesis:** Fleet efficiency will be lowest in Jan/Feb due to snow.
* **Reality:** The fleet is **most efficient in Winter** (Dec Peak: ~$8.48/mile) and **least efficient in Summer** (Aug Low: ~$7.66/mile).
* **Root Cause:** The "Work-from-Hamptons" effect removes high-value business commuters in August.

### 2. Infrastructure: The "Gravity Center" Map
* **Finding:** Demand is hyper-concentrated in a contiguous block (Zones 161, 237, 236).
* **Strategy:** Building cheap depots in Queens is a strategic error. Secured leases in **Zone 161 (Midtown)** and **Zone 236 (UES)** are mandatory to capture ~220,000 monthly terminations.

<img width="1549" height="1041" alt="image" src="https://github.com/user-attachments/assets/f57eec9a-1738-42ca-9760-c8032a0bbe4f" />

---

## 🤖 Advanced Engineering Modules

### 🔮 Module A: The "Oracle" Demand Predictor
* **Model:** Random Forest Regressor (Scikit-Learn).
* **Performance:** Mean Absolute Error (MAE) of **+/- 20.5 rides** (95% Accuracy).
* **Deployment:** Accessible via the live Streamlit interface.

### 🚦 Module B: The Airport Arbitrage Algorithm
**The Problem:** Drivers often wait 60+ minutes at JFK for a standard fare, unknowingly losing money compared to city driving.
**The Solution:** A dynamic **Decision Matrix** that calculates the "Mathematical Breakeven Point" for waiting in the airport queue.

* <img width="1276" height="593" alt="image" src="https://github.com/user-attachments/assets/0bde71b1-6c66-4762-8a15-5e867a6e4574" />


#### 📋 Operational Look-Up Table (JFK Airport)
| Projected Fare ($) | Max Permissible Wait | Strategy Recommendation |
| :--- | :--- | :--- |
| **$50** | 21 min | ⛔ **Return to City Immediately** |
| **$60** | 34 min | ⚠️ **Strict Limit** (Reject if queue > 35m) |
| **$80** | 61 min | ✅ **Wait up to 1 Hour** |
| **$110+** | 100+ min | 🚀 **Max Priority** |

---

## 🔮 Future Roadmap (v2.0)
* **Real-Time API:** Integrate with OpenWeatherMap API for live storm tracking.
* **Battery Degradation Model:** Factor in battery health cost per mile for deeper P&L analysis.
* **Competitor Analysis:** Add Uber/Lyft pricing scraping to adjust Surge Multipliers dynamically.
  
---

## 🛠 Technical Architecture

```bash
├── .streamlit/             # App Theme Config (Dark Mode / Colors)
├── Data/                   # Raw Parquet files (GitIgnored)
├── Visualizations/         # High-res charts & Dashboard Screenshots
├── app.py                  # Streamlit Interactive Dashboard (Main App)
├── Tesla Robotaxi project.ipynb  # Core Analysis & EDA Notebook
├── requirements.txt        # Python dependencies
└── README.md               # Documentation