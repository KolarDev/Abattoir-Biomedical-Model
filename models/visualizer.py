import matplotlib.pyplot as plt

def plot_biomechanical_chain(coords, case_name="Cutting Operation"):
    """
    Generates a professional Matplotlib plot for the 4-link kinematic chain.
    """
    fig, ax = plt.subplots(figsize=(7, 9))
    
    # Extract points
    sh = coords["shoulder"]
    el = coords["elbow"]
    wr = coords["wrist"]
    kn = coords["knife"]
    
    x_vals = [sh[0], el[0], wr[0], kn[0]]
    y_vals = [sh[1], el[1], wr[1], kn[1]]
    
    # Plot segments
    ax.plot(x_vals, y_vals, '-o', color='#1a1a1a', linewidth=4, markersize=12, label="Link Chain")
    
    # Accentuate the knife tip
    ax.plot(kn[0], kn[1], 'r*', markersize=15, label="Knife Tip (P)")
    
    # Labeling joints
    ax.annotate('Shoulder', (sh[0], sh[1]), textcoords="offset points", xytext=(-10,10), fontweight='bold')
    ax.annotate('Elbow (E)', (el[0], el[1]), textcoords="offset points", xytext=(10,-10))
    ax.annotate('Wrist (W)', (wr[0], wr[1]), textcoords="offset points", xytext=(10,-10))
    ax.annotate('Knife (P)', (kn[0], kn[1]), textcoords="offset points", xytext=(10,10), color='red')

    # Reference Lines
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    
    # Styling
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_title(f"Biomechanical Link-Joint Model: {case_name}", fontsize=14, pad=20)
    ax.set_xlabel("Horizontal Position (cm)")
    ax.set_ylabel("Vertical Position (cm)")
    
    # Clean up the view
    padding = 20
    ax.set_xlim(min(x_vals)-padding, max(x_vals)+padding)
    ax.set_ylim(min(y_vals)-padding, max(y_vals)+padding)
    
    return fig