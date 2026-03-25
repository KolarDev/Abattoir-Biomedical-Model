import streamlit as st
from models.calculator import calculate_model_1, calculate_model_2, calculate_model_3, calculate_model_4

# UI Setup
st.set_page_config(page_title="Abattoir Biomechanics", layout="wide")
st.title("Worker Biomechanical Simulator")

# Sidebar for Anthropometrics
st.sidebar.header("Body Measurements (cm)")
sel = st.sidebar.number_input("Shoulder to Elbow (SEL)", value=30.0)
ewl = st.sidebar.number_input("Elbow to Wrist (EWL)", value=25.0)
hl = st.sidebar.number_input("Hand Length (HL)", value=18.0)
sh = st.sidebar.number_input("Shoulder Height (SH)", value=150.0)

tab1, tab2 = st.tabs(["Case I: Cutting", "Case II: Deboning"])

with tab1:
    st.header("Case I: Cutting Operation")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # THE FIX: Added Arm Angle (A) slider
        a_angle = st.slider("Arm Angle (A)", 0, 180, 45, help="Angle at the elbow joint")
        q_angle = st.slider("Shoulder Angle (Q)", 0, 180, 90, help="Angle at the shoulder/hip")
        
        # Calculations using your fixed logic
        thh = calculate_model_1(sel, ewl, hl, sh, a_angle, q_angle)
        thv = calculate_model_2(sh, q_angle)
        
        st.metric("Horizontal Distance (THh)", f"{thh:.2f} cm")
        st.metric("Vertical Distance (THv)", f"{thv:.2f} cm")

    with col2:
        st.info("Visual representation will appear here.")
        # Later, we will add the Plotly stick-figure graph here

with tab2:
    st.header("Case II: Deboning Operation")

    col1, col2 = st.columns([1, 2])

    with col1:
        q_angle2 = st.slider("Shoulder Angle (Q)", 0, 180, 90, key="q2")
        theta_angle = st.slider("Elbow Angle (θ)", 0, 180, 110)

        # Calculations
        ehh = calculate_model_3(sel, sh, q_angle2, theta_angle)
        ehv = calculate_model_4(sel, sh, q_angle2, theta_angle)

        st.metric("Horizontal Elbow Distance (EHh)", f"{ehh:.2f} cm")
        st.metric("Vertical Elbow Distance (EHv)", f"{ehv:.2f} cm")

    with col2:
        st.info("Visualization coming next (arm model)")