import os
import joblib
from virtual_sensor import generate_sensor_data
import pandas as pd

# Get absolute path for model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'crop_model.pkl')

model = joblib.load(MODEL_PATH)

def predict_crop():
    data = generate_sensor_data()
    input_df = pd.DataFrame([data])[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    prediction = model.predict(input_df)[0]
    return data, prediction

def recommend_fertilizer(N, P, K):
    ideal_NPK = {
        'N': 90,
        'P': 40,
        'K': 40
    }

    recommendations = []

    if N < ideal_NPK['N']:
        recommendations.append("Nitrogen")
    if P < ideal_NPK['P']:
        recommendations.append("Phosphorus")
    if K < ideal_NPK['K']:
        recommendations.append("Potassium")

    if not recommendations:
        return "Soil nutrient levels are optimal. No fertilizer needed."
    
    return f"Recommended: Add {' + '.join(recommendations)} based fertilizer."