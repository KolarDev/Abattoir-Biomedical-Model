import numpy as np

def calculate_model_1(shl, ewl, hl, sh, q_deg):
    # Convert degrees to radians for Python's math functions
    q_rad = np.radians(q_deg)
    
    # Example: THh = [(SHL)^2 + (EWL - 0.5 HL)^2 + 2(SHL)(EWL - 0.5HL)]^1/2 + [SH * Cos(180 - Q)]
    # Note: Using np.sqrt for the [...]^1/2 part
    term1 = np.sqrt(shl**2 + (ewl - 0.5*hl)**2 + 2*shl*(ewl - 0.5*hl))
    term2 = sh * np.cos(np.radians(180) - q_rad)
    
    return term1 + term2

# You can add Model 2, 3, and 4 as similar functions here