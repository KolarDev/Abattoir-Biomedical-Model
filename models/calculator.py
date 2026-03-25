import numpy as np

def calculate_model_1(sel, ewl, hl, sh, a_deg, q_deg):
    """
    Horizontal Distance of Table Height (THh)
    """
    A = np.radians(a_deg)
    Q = np.radians(q_deg)

    # Corrected term1: Uses (EWL + 0.5HL) and the Law of Cosines
    term1 = np.sqrt(
        sel**2 + 
        (ewl + 0.5 * hl)**2 - 
        2 * sel * (ewl + 0.5 * hl) * np.cos(A)
    )

    # Corrected term2: Horizontal projection of the shoulder
    # Note: cos(180 - Q) is -cos(Q)
    term2 = sh * np.cos(np.pi - Q) 

    return term1 - term2

def calculate_model_2(sh, q_deg):
    """Vertical Distance of Table Height (THv)"""
    Q = np.radians(q_deg)
    return sh * np.sin(Q)

def calculate_model_3(sel, sh, q_deg, theta_deg):
    """Horizontal Elbow Position (EHh)"""

    Q = np.radians(q_deg)
    theta = np.radians(theta_deg)

    shoulder_x = sh * np.cos(np.pi - Q)

    elbow_x = shoulder_x + sel * np.cos(theta - np.pi/2)

    return elbow_x


def calculate_model_4(sel, sh, q_deg, theta_deg):
    """Vertical Elbow Position (EHv)"""

    Q = np.radians(q_deg)
    theta = np.radians(theta_deg)

    shoulder_y = sh * np.sin(np.pi - Q)

    elbow_y = shoulder_y - sel * np.sin(theta - np.pi/2)

    return elbow_y