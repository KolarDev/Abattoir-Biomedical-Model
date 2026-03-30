import numpy as np

# --- CASE I: CUTTING (Model 1 & 2) ---
def calculate_model_1(sel, ewl, hl, sh, theta_deg, q_deg):
    """Horizontal Distance of Table Height (THh / p)"""
    Q = np.radians(q_deg)
    theta = np.radians(theta_deg)
    L2 = ewl + 0.5 * hl
    
    # Expanded Formula: SH*cos(180-Q) + (SEL + L2)*cos(theta-90)
    term1 = sh * np.cos(np.pi - Q)
    term2 = (sel + L2) * np.cos(theta - np.pi/2)
    return term1 + term2

def calculate_model_2(sel, ewl, hl, sh, theta_deg, q_deg):
    """Vertical Distance of Table Height (THv / h)"""
    Q = np.radians(q_deg)
    theta = np.radians(theta_deg)
    L2 = ewl + 0.5 * hl
    
    # Expanded Formula: SH*sin(180-Q) - (SEL + L2)*sin(theta-90)
    term1 = sh * np.sin(np.pi - Q)
    term2 = (sel + L2) * np.sin(theta - np.pi/2)
    return term1 - term2

# --- CASE II: DEBONING (Model 3 & 4) ---
def calculate_model_3(sel, sh, q_deg, theta_deg):
    """Horizontal distance of Elbow Height (EHh / w)"""
    Q = np.radians(q_deg)
    theta = np.radians(theta_deg)
    
    # Expanded Formula: SH*cos(180-Q) + SEL*cos(theta-90)
    term1 = sh * np.cos(np.pi - Q)
    term2 = sel * np.cos(theta - np.pi/2)
    return term1 + term2

def calculate_model_4(sel, sh, q_deg, theta_deg):
    """Vertical distance of Elbow Height (EHv / q)"""
    Q = np.radians(q_deg)
    theta = np.radians(theta_deg)
    
    # Expanded Formula: SH*sin(180-Q) - SEL*sin(theta-90)
    term1 = sh * np.sin(np.pi - Q)
    term2 = sel * np.sin(theta - np.pi/2)
    return term1 - term2