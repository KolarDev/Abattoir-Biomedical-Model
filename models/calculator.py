import numpy as np

def calculate_kinematics(Lu, Lf, Lh, Lk, angles_deg):
    """Computes positions (x, y) for Elbow, Wrist, and Knife Tip."""
    t1, t2, t3, t4 = np.radians(angles_deg)
    
    # xE = Lu sin(t1), yE = -Lu cos(t1)
    xe = Lu * np.sin(t1)
    ye = -Lu * np.cos(t1)
    
    # xW = xE + Lf sin(t1+t2), yW = yE - Lf cos(t1+t2)
    xw = xe + Lf * np.sin(t1 + t2)
    yw = ye - Lf * np.cos(t1 + t2)
    
    # xP = xW + (Lh+Lk) sin(t1+t2+t3+t4), yP = yW - (Lh+Lk) cos(t1+t2+t3+t4)
    L_total = Lh + Lk
    xp = xw + L_total * np.sin(t1 + t2 + t3 + t4)
    yp = yw - L_total * np.cos(t1 + t2 + t3 + t4)
    
    return {
        "shoulder": (0, 0), "elbow": (xe, ye), 
        "wrist": (xw, yw), "knife": (xp, yp)
    }

def calculate_torques(pos, Fx, Fy):
    """Calculates tau = Fx(yp - yi) - Fy(xp - xi) for each joint i."""
    xp, yp = pos["knife"]
    
    # Shoulder (Origin 0,0)
    ts = Fx * (yp - 0) - Fy * (xp - 0)
    
    # Elbow
    xe, ye = pos["elbow"]
    te = Fx * (yp - ye) - Fy * (xp - xe)
    
    # Wrist
    xw, yw = pos["wrist"]
    tw = Fx * (yp - yw) - Fy * (xp - xw)
    
    return ts, te, tw

def calculate_resultant_force(Fx, Fy):
    """Calculates Magnitude (Fc) and Angle of the knife force."""
    magnitude = np.sqrt(Fx**2 + Fy**2)
    angle = np.degrees(np.arctan2(Fy, Fx))
    return magnitude, angle