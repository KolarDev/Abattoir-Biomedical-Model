import numpy as np

# --- CASE I: CUTTING (Model 1 & 2) ---
def calculate_model_1(sel, ewl, hl, sh, a_deg, q_deg):
    """Horizontal Distance of Table Height (THh)"""
    A, Q = np.radians(a_deg), np.radians(q_deg)
    # Vector: HRP_x -> Shoulder_x -> Table_x
    term1 = np.sqrt(sel**2 + (ewl + 0.5 * hl)**2 - 2 * sel * (ewl + 0.5 * hl) * np.cos(A))
    term2 = sh * np.cos(np.pi - Q)
    return term1 - term2

def calculate_model_2(sh, q_deg):
    """Vertical Distance of Table Height (THv)"""
    Q = np.radians(q_deg)
    return sh * np.sin(Q)

# --- CASE II: DEBONING (Model 3 & 4) ---
# Rebuilt using Vector Kinematics: HRP -> Shoulder -> Elbow
def calculate_model_3(sel, sh, q_deg, theta_deg):
    """Horizontal distance of Elbow (EHh)"""
    Q, theta = np.radians(q_deg), np.radians(theta_deg)
    # 1. Locate Shoulder X
    sx = sh * np.cos(np.pi - Q)
    # 2. Offset by Upper Arm projection
    ex = sx + sel * np.cos(theta - np.pi/2)
    return ex

def calculate_model_4(sel, sh, q_deg, theta_deg):
    """Vertical distance of Elbow (EHv)"""
    Q, theta = np.radians(q_deg), np.radians(theta_deg)
    # 1. Locate Shoulder Y
    sy = sh * np.sin(np.pi - Q)
    # 2. Offset by Upper Arm projection
    ey = sy - sel * np.sin(theta - np.pi/2)
    return ey