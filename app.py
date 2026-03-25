import streamlit as st
from models.calculator import calculate_model_1

st.title("Abattoir Worker Biomechanical Simulator")

# Sidebar for Inputs
st.sidebar.header("Input Parameters (cm/deg)")
shl = st.sidebar.number_input("Shoulder to Elbow Length (SEL)", value=30.0)
ewl = st.sidebar.number_input("Elbow to Wrist Length (EWL)", value=25.0)
hl = st.sidebar.number_input("Hand Length (HL)", value=18.0)
sh = st.sidebar.number_input("Shoulder Height (SH)", value=150.0)
q_angle = st.sidebar.slider("Shoulder Angle (Q)", 0, 180, 90)

# Calculation
thh_result = calculate_model_1(shl, ewl, hl, sh, q_angle)

# Output
st.subheader("Results")
st.success(f"Horizontal Distance of Table Height (THh): {thh_result:.2f}")