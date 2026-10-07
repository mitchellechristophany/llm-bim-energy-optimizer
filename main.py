import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.ensemble import RandomForestRegressor

app = FastAPI(title="BIM Energy Optimizer API")

# Mock Trained ML Model for Building Energy Performance
X_dummy = np.random.rand(100, 3) # Area (sqft), Insulation R-value, Window-to-Wall Ratio
y_dummy = X_dummy @ np.array([50.0, -30.0, 80.0]) + 100
rf_model = RandomForestRegressor().fit(X_dummy, y_dummy)

class BuildingConfig(BaseModel):
    area_sqft: float
    insulation_r_value: float
    window_wall_ratio: float

@app.post("/predict_energy")
def predict_energy(config: BuildingConfig):
    features = [[config.area_sqft, config.insulation_r_value, config.window_wall_ratio]]
    predicted_kwh = float(rf_model.predict(features)[0])
    
    # Rule-Based LLM/GenAI Recommendation Proxy
    recommendations = []
    if config.insulation_r_value < 15:
        recommendations.append("Upgrade wall insulation to R-20+ to reduce thermal loss.")
    if config.window_wall_ratio > 0.4:
        recommendations.append("Consider low-E glazing to optimize window solar heat gain coefficient.")
        
    return {
        "estimated_annual_kwh": round(predicted_kwh, 2),
        "sustainability_advice": recommendations if recommendations else ["Building envelope parameters are optimized."]
    }
