# Abattoir Worker Biomechanical Simulator

A mathematical modeling tool built in Python to simulate the ergonomic positioning of abattoir workers during cutting and deboning operations. This tool calculates the Horizontal ($TH_h$) and Vertical ($TH_v$) distances relative to the Hip Reference Point (HRP).

## 📂 Project Structure

```text
abattoir-biomechanics/
├── app.py              # Main Streamlit Web Interface
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
├── models/
│   ├── calculator.py   # Math Engine (Models 1-4)
│   └── visualizer.py   # Matplotlib Link-Joint Plotter
└── assets/             # Research diagrams (Fig 4.7, 4.8)
```

## 🚀 Installation & Usage1. Setup EnvironmentBashpython -m venv venv
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
2. Install DependenciesBashpip install -r requirements.txt
3. Run the SimulatorBashstreamlit run app.py
📊 MethodologyThis calculator utilizes Biomechanical Link-Segment Modeling:Model 1 & 2: Calculate table height based on Shoulder Height (SH) and flex angles (Q, A).Law of Cosines: Used to determine the extension of the upper limb segments.Coordinate System: The Hip Reference Point (HRP) is treated as the origin $(0,0)$.⚠️ Notes for CorrectionThe mathematical models are currently in a "draft and verify" phase.Equations in models/calculator.py are being cross-referenced with Figure 4.7 and 4.8 of the research document.Ensure all angles are input in Degrees (the system converts them to Radians internally).
---

### Final Check
* **Visualizer:** By plotting the segments, you’ll immediately see if the "Table Height" makes sense. If the wrist is higher than the shoulder but the model says the table is at 90cm, you'll know there's a sign error in the math.
* **Streamlit:** It will now show the numbers on the left and the drawing on the right.
