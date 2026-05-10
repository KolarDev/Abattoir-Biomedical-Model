import streamlit as st
from models.calculator import calculate_kinematics, calculate_torques, calculate_resultant_force
from models.visualizer import plot_biomechanical_chain

st.set_page_config(page_title="Abattoir Biomechanics Lab", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; color: #1e3d59; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #dce1e3;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🥩 Biomechanical Analysis of Abattoir Workers")
st.write("Kinematic 4-Link Serial Chain: Shoulder ➔ Elbow ➔ Wrist ➔ Knife Tip")

# --- SIDEBAR: Parameters ---
with st.sidebar:
    st.header("📏 Segment Lengths (cm)")
    Lu = st.slider("Upper Arm (Lu)", 20.0, 50.0, 32.5)
    Lf = st.slider("Forearm (Lf)", 20.0, 50.0, 28.0)
    Lh = st.slider("Hand Length (Lh)", 5.0, 25.0, 18.0)
    Lk = st.slider("Knife Length (Lk)", 5.0, 30.0, 15.0)
    
    st.header("📐 Joint Posture (Degrees)")
    q1 = st.slider("Shoulder Flexion (θ1)", -90, 90, 30)
    q2 = st.slider("Elbow Flexion (θ2)", -90, 90, 45)
    q3 = st.slider("Wrist Extension (θ3)", -45, 45, 10)
    q4 = st.slider("Hand/Knife Angle (θ4)", -45, 45, 5)
    
    st.header("💥 Applied Forces (N)")
    Fx_input = st.number_input("Horizontal Force (Fx)", value=15.0)
    Fy_input = st.number_input("Vertical Force (Fy)", value=-45.0)

# --- ENGINE: Processing ---
angles = [float(q1), float(q2), float(q3), float(q4)]
coords = calculate_kinematics(Lu, Lf, Lh, Lk, angles)

# Note: We name these tau_s, tau_e, tau_w to be consistent
tau_s, tau_e, tau_w = calculate_torques(coords, float(Fx_input), float(Fy_input))
fc_mag, fc_ang = calculate_resultant_force(float(Fx_input), float(Fy_input))

# --- UI: Display ---
col_vis, col_data = st.columns([3, 2])

with col_vis:
    st.subheader("Link-Joint Kinematic Model")
    fig = plot_biomechanical_chain(coords)
    st.pyplot(fig, width='stretch')

with col_data:
    st.subheader("Biomechanical Metrics")
    
    with st.container():
        st.info("**Internal Joint Torques (τ)**")
        c1, c2, c3 = st.columns(3)
        
        # FIX: Using tau_s, tau_e, tau_w consistently now
        c1.metric("Shoulder Torque", f"{tau_s:.1f} N·cm")
        c2.metric("Elbow Torque", f"{tau_e:.1f} N·cm")
        c3.metric("Wrist Torque", f"{tau_w:.1f} N·cm")
        
        st.divider()
        
        st.info("**External Cutting Force (Fc)**")
        f1, f2 = st.columns(2)
        f1.metric("Total Magnitude", f"{fc_mag:.2f} N")
        f2.metric("Cut Direction", f"{fc_ang:.1f}°")
        
        st.divider()
        
        st.success(f"""
        **System Feedback:**
        - **Hand Position (X, Y):** ({coords['wrist'][0]:.1f}, {coords['wrist'][1]:.1f})
        - **Knife Tip Position (X, Y):** ({coords['knife'][0]:.1f}, {coords['knife'][1]:.1f})
        """)