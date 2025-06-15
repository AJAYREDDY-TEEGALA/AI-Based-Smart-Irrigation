
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import streamlit as st
from prediction_engine import predict_crop, recommend_fertilizer
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Farming Assistant", layout="centered")
st.title("🌾 Smart Farming Assistant")
st.markdown("Real-time AI-powered crop suggestion based on simulated sensor data.")

if st.button("Simulate Sensors & Predict"):
    sensor_data, prediction = predict_crop()
    
    st.subheader("\U0001F321️ Virtual Sensor Readings")
    st.write("### Sensor Data Table")
    st.table(sensor_data.items())

    # Bar Chart of NPK values
    st.write("### Nutrient (NPK) Levels")
    fig, ax = plt.subplots()
    nutrients = ['N', 'P', 'K']
    values = [sensor_data['N'], sensor_data['P'], sensor_data['K']]
    ideal = [90, 40, 40]
    bar_width = 0.35

    ax.bar(nutrients, values, bar_width, label='Current')
    ax.bar([i + bar_width for i in range(len(ideal))], ideal, bar_width, label='Ideal')
    ax.set_ylabel('Value')
    ax.set_title('NPK vs Ideal Levels')
    ax.legend()
    st.pyplot(fig)

    st.subheader("🌱 AI Prediction")
    st.success(f"Recommended Crop: **{prediction}**")

    st.subheader("🧪 Fertilizer Suggestion")
    fert_suggestion = recommend_fertilizer(sensor_data['N'], sensor_data['P'], sensor_data['K'])
    st.info(fert_suggestion)
    st.caption("Simulated sensor data is based on real-world farming datasets.")