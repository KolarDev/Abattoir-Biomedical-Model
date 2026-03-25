import streamlit as st
from models.calculator import calculate_model_1, calculate_model_2, calculate_model_3, calculate_model_4
from models.visualizer import plot_worker

st.set_page_config(page_title="Abattoir Biomechanics Lab", layout="wide")
st.title("Biomechanics Simulator for Abattoir Workers")

# Global Sidebar Inputs
st.sidebar.header("Anthropometric Data (cm)")
sh = st.sidebar.number_input("Shoulder Height (SH)", value=150.0)
sel = st.sidebar.number_input("Shoulder to Elbow (SEL)", value=35.0)
ewl = st.sidebar.number_input("Elbow to Wrist (EWL)", value=25.0)
hl = st.sidebar.number_input("Hand Length (HL)", value=18.0)

tab1, tab2 = st.tabs(["Case I: Cutting", "Case II: Deboning"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Controls")
        q_angle = st.slider("Shoulder Angle (Q)", 0, 180, 90, key="q_cut")
        a_angle = st.slider("Arm Angle (A)", 0, 180, 45, key="a_cut")
        
        # Math Results
        thh = calculate_model_1(sel, ewl, hl, sh, a_angle, q_angle)
        thv = calculate_model_2(sh, q_angle)
        
        st.metric("Horizontal (THh)", f"{thh:.2f} cm")
        st.metric("Vertical (THv)", f"{thv:.2f} cm")

    with col2:
        fig = plot_worker(sh, sel, ewl, hl, q_angle, a_angle, case="Cutting")
        st.pyplot(fig)

with tab2:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Controls")
        q_deb = st.slider("Shoulder Angle (Q)", 0, 180, 100, key="q_deb")
        theta_deb = st.slider("Elbow Angle (θ)", 0, 180, 60, key="t_deb")
        
        # Math Results (Your Rebuilt Model 3 & 4)
        ehh = calculate_model_3(sel, sh, q_deb, theta_deb)
        ehv = calculate_model_4(sel, sh, q_deb, theta_deb)
        
        st.metric("Elbow Horizontal (EHh)", f"{ehh:.2f} cm")
        st.metric("Elbow Vertical (EHv)", f"{ehv:.2f} cm")

    with col2:
        fig = plot_worker(sh, sel, ewl, hl, q_deb, theta_deb, case="Deboning")
        st.pyplot(fig)