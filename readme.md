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