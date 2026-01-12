# 🚖 Tesla Robotaxi Fleet Optimization: NYC Market Analysis
![Status](https://img.shields.io/badge/Status-Complete-success) ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Library](https://img.shields.io/badge/Library-Scikit--Learn%20%7C%20Pandas%20%7C%20Streamlit-orange)

### 📌 Executive Summary
**Objective:** Engineer a fleet positioning strategy for a hypothetical Tesla Robotaxi network in NYC.
**Scope:** Analyzed **38 Million** trip records (Jan–Dec 2024) to solve the "Deadhead Mile" profitability crisis.
**Outcome:** Identified **$10M+ in annual efficiency gains** by disproving the "Winter Weather" penalty myth and optimizing summer fleet allocation.

---

### 💰 Business Impact Analysis
| Problem Detected | Data Evidence | Strategic Solution | Est. Value Impact |
| :--- | :--- | :--- | :--- |
| **"Summer Slump"** | Efficiency ($/Mile) drops **9.6%** in August vs. December. | **Dynamic Cap:** Reduce Midtown fleet by 30% in Q3; redeploy to Airports. | **$4.2M / Year** (Saved in depreciation & ops) |
| **"Missing Bankers"** | Midtown Commuter demand collapses **34.8%** in August. | **Shift Strategy:** Move charging windows to 4 PM–6 PM to align with "Nightlife" demand. | **$3.5M / Year** (Recovered revenue) |
| **Charging Gaps** | Cars drive ~3.2 miles empty to charge. | **Gravity Mapping:** Identified 5 optimal zones for vertical charging hubs. | **$2.8M / Year** (Energy & Time savings) |
| **Airport Queues** | Drivers wait 60+ mins for $50 fares. | **Arbitrage Algo:** "93-Minute Rule" auto-rejects unprofitable queues. | **+12% Utilization** (Fleetwide) |

---

### 📊 Key Findings

#### 1. The "Winter Penalty" Myth (Disproven)
* **Hypothesis:** *Fleet efficiency will be lowest in Jan/Feb due to snow.*
* **Reality:** The fleet is **most efficient in Winter** (Dec Peak: ~$8.48/mile) and **least efficient in Summer** (Aug Low: ~$7.66/mile).
* **Root Cause:** The "Work-from-Hamptons" effect removes high-value business commuters in August.
![Efficiency Trend](Visualizations/efficiency_trend_2024.png)

#### 2. The "Missing Banker" Effect
* **Metric:** Midtown (Zone 237) ride volume plummets by **64,000 trips** in August.
* **Behavior:** The classic "9-to-5" rush hour spikes vanish in summer telemetry.
![Rush Hour Collapse](Visualizations/rush_hour_collapse.png)

#### 3. Infrastructure: The "Gravity Center" Map
* **Finding:** Demand is hyper-concentrated in a contiguous block (Zones 161, 237, 236).
* **Strategy:** Building cheap depots in Queens is a strategic error. Secured leases in **Zone 161 (Midtown)** and **Zone 236 (UES)** are mandatory to capture ~220,000 monthly terminations.
![Supercharger Map](Visualizations/supercharger_density_map.png)

---

### 🤖 Advanced Engineering Modules

#### 🔮 Module A: The "Oracle" Demand Predictor (Machine Learning)
* **Model:** Random Forest Regressor (Scikit-Learn).
* **Performance:** Mean Absolute Error (MAE) of **+/- 20.5 rides** (95% Accuracy).
* **Deployment:** Model is accessible via the `app.py` Streamlit interface.

#### 🚦 Module B: The Airport Arbitrage Algorithm (Strategy)
* **The Problem:** Drivers often wait 60+ minutes at JFK for a standard fare, unknowingly losing money compared to city driving.
* **The Solution:** Developed a dynamic **Decision Matrix** that calculates the "Mathematical Breakeven Point" for waiting in the airport queue.

**📋 Operational Look-Up Table (JFK Airport):**
| Projected Fare ($) | Max Permissible Wait | Strategy Recommendation |
| :--- | :--- | :--- |
| **$50** | 21 min | ⛔ **Return to City Immediately** |
| **$60** | 34 min | ⚠️ **Strict Limit** (Reject if queue > 35m) |
| **$70** | 48 min | ✅ **Standard Wait** |
| **$80** | 61 min | ✅ **Wait up to 1 Hour** |
| **$90** | 75 min | 💎 **High Priority** |
| **$100** | 88 min | 💎 **High Priority** |
| **$110** | 101 min | 🚀 **Max Priority** |
| **$120** | 114 min | 🚀 **Max Priority** |

* **Visual:** `Visualizations/strategy_airport_wait.png`
*(See the "Red Line" in the chart for the 1-hour breakeven threshold)*

---

### 🛠 Technical Architecture
```bash
├── Data/                   # Raw Parquet files (GitIgnored)
├── Models/                 # Serialized .pkl machine learning models
├── Visualizations/         # High-res charts (Seaborn/Matplotlib)
├── app.py                  # Streamlit Interactive Dashboard
├── analysis_notebook.ipynb # Core Logic & EDA
├── requirements.txt        # Python dependencies
└── README.md               # You are here