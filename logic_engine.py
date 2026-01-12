import numpy as np
def predict_metrics(month, day, hour, surge, weather_cond):
    """
    Predicts demand, revenue, and profit based on inputs.
    """
    base_demand = 400
    # 1. Seasonality Logic (The "Story" Factor)
    if month in ["July", "August"]:
        base_demand *= 0.75 # "The Missing Banker Effect" (Summer Dip)
    elif month in ["November", "December"]:
        base_demand *= 1.25 # Holiday Rush
    elif month in ["March", "April", "May"]:
        base_demand *= 1.10 # Spring Business Peak
    # 2. Time Logic
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        if 7 <= hour <= 10: base_demand += 300 # AM Rush
        if 16 <= hour <= 19: base_demand += 450 # PM Rush
    if day in ["Friday", "Saturday"] and hour >= 20: base_demand += 400 # Nightlife
    # 3. Weather Logic
    if weather_cond == "Rain": base_demand *= 1.15
    if weather_cond == "Snowstorm": base_demand *= 0.9 
    # 4. Economics
    elasticity = 1.0 - (surge * 0.1) 
    final_demand = int(base_demand * elasticity)
    # Random Noise
    final_demand += np.random.randint(-15, 15)
    gross_revenue = final_demand * (22 * surge)
    profit = gross_revenue - (final_demand * 4.50)
    return final_demand, gross_revenue, profit