import streamlit as st
from src.predictor.predict import Predictor

st.set_page_config(page_title="Concrete Strength Predictor", layout="centered")

st.title("Ceramic Waste Concrete Strength Predictor")
st.markdown("Enter the concrete mix design parameters below to predict **compressive strength (MPa)**.")

predictor = Predictor()

# Define input fields
cement = st.number_input("Cement (kg/m³)", min_value=0.0, step=1.0)
flyash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, step=1.0)
ggbs = st.number_input("GGBS (kg/m³)", min_value=0.0, step=1.0)
mk = st.number_input("Metakaolin (kg/m³)", min_value=0.0, step=1.0)
water = st.number_input("Water (kg/m³)", min_value=0.0, step=1.0)
water_tcm = st.number_input("Water / TCM Ratio", min_value=0.0, max_value=1.0, step=0.01)
sp = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, step=0.1)
vma = st.number_input("VMA (kg/m³)", min_value=0.0, step=0.1)
nca_20_down = st.number_input("Natural CA 20mm Down (kg/m³)", min_value=0.0, step=1.0)
nca_10_down = st.number_input("Natural CA 10mm Down (kg/m³)", min_value=0.0, step=1.0)
rca_20_down = st.number_input("Recycled CA 20mm Down (kg/m³)", min_value=0.0, step=1.0)
rca_10_down = st.number_input("Recycled CA 10mm Down (kg/m³)", min_value=0.0, step=1.0)
sand = st.number_input("Fine Aggregate / Sand (kg/m³)", min_value=0.0, step=1.0)
age = st.number_input("Curing Age (days)", min_value=1, step=1)

if st.button("Predict Strength"):
    input_data = {
        "cement": cement,
        "flyash": flyash,
        "ggbs": ggbs,
        "mk": mk,
        "water": water,
        "water_tcm": water_tcm,
        "sp": sp,
        "vma": vma,
        "nca_20_down": nca_20_down,
        "nca_10_down": nca_10_down,
        "rca_20_down": rca_20_down,
        "rca_10_down": rca_10_down,
        "sand": sand,
        "age": age
    }

    prediction = predictor.predict(input_data)
    st.success(f"Predicted Compressive Strength: **{prediction:.2f} MPa**")
