import matplotlib.pyplot as plt
import numpy as np

def plot_worker(sh, sel, ewl, hl, q_deg, theta_deg, case="Cutting"):
    fig, ax = plt.subplots(figsize=(6, 8))
    
    # 1. HRP (Origin)
    hrp = (0, 0)
    
    # 2. Shoulder Position (Sync with 180-Q)
    Q = np.radians(q_deg)
    sh_x = sh * np.cos(np.pi - Q)
    sh_y = sh * np.sin(np.pi - Q)
    
    # 3. Elbow Position (Sync with theta-90)
    theta = np.radians(theta_deg)
    elb_x = sh_x + sel * np.cos(theta - np.pi/2)
    elb_y = sh_y - sel * np.sin(theta - np.pi/2)
    
    # 4. Wrist/Forearm Position
    wrist_x, wrist_y = None, None
    if case == "Cutting":
        L2 = ewl + 0.5 * hl
        wrist_x = elb_x + L2 * np.cos(theta - np.pi/2)
        wrist_y = elb_y - L2 * np.sin(theta - np.pi/2)

    # --- DRAWING ---
    ax.plot([hrp[0], sh_x], [hrp[1], sh_y], 'k-o', linewidth=4, label='Torso (HRP-Shoulder)')
    ax.plot([sh_x, elb_x], [sh_y, elb_y], 'b-o', linewidth=3, label='Upper Arm (SEL)')
    
    if wrist_x is not None:
        ax.plot([elb_x, wrist_x], [elb_y, wrist_y], 'g-o', linewidth=3, label='Forearm/Hand (L2)')
        if case == "Cutting":
            ax.axhline(y=wrist_y, color='red', linestyle='--', alpha=0.5, label='Table Surface (THv)')

    ax.set_aspect('equal')
    limit = sh + sel + 20
    ax.set_xlim(-limit/2, limit/2)
    ax.set_ylim(-10, limit)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='upper left', fontsize='small')
    ax.set_title(f"Biomechanical Model: {case} Operation", fontsize=12)
    
    return fig