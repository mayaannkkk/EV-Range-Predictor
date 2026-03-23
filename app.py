import streamlit as st
import pickle
import pandas as pd

# Load model
with open('pipe.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🚗 EV Price Predictor")

st.header("Enter Car Details")

# --- Numeric Inputs ---
top_speed = st.number_input("Top Speed (km/h)", value=150)
battery = st.number_input("Battery Capacity (kWh)", value=50.0)
torque = st.number_input("Torque (Nm)", value=200.0)
efficiency = st.number_input("Efficiency (Wh/km)", value=150.0)
acceleration = st.number_input("0-100 Acceleration (s)", value=8.0)

fast_charge = st.number_input("Fast Charging Power (kW DC)", value=50.0)
towing = st.number_input("Towing Capacity (kg)", value=500.0)
cargo = st.number_input("Cargo Volume (L)", value=400.0)

length = st.number_input("Length (mm)", value=4000)
width = st.number_input("Width (mm)", value=1800)
height = st.number_input("Height (mm)", value=1600)

# --- Categorical Inputs ---
segment = st.selectbox("Segment", ['B - Compact', 'JB - Compact', 'JC - Medium', 'JE - Executive',
       'JD - Large', 'F - Luxury', 'D - Large', 'E - Executive',
       'C - Medium', 'JF - Luxury', 'N - Passenger Van', 'A - Mini',
       'JA - Mini', 'G - Sports', 'I - Luxury'])
body_type = st.selectbox("Body Type", ['Hatchback', 'SUV', 'Station/Estate', 'Liftback Sedan', 'Sedan',
       'Small Passenger Van', 'Cabriolet', 'Coupe'])

# --- Prediction ---
if st.button("Predict Price"):

    input_df = pd.DataFrame(
        [[top_speed, battery, torque, efficiency, acceleration,
          fast_charge, towing, cargo, segment,
          length, width, height, body_type]],
        columns=[
            'top_speed_kmh', 'battery_capacity_kWh', 'torque_nm',
            'efficiency_wh_per_km', 'acceleration_0_100_s',
            'fast_charging_power_kw_dc', 'towing_capacity_kg',
            'cargo_volume_l', 'segment',
            'length_mm', 'width_mm', 'height_mm', 'car_body_type'
        ]
    )

    prediction = model.predict(input_df)

    st.success(f"💰 Predicted Price: {prediction[0]}")