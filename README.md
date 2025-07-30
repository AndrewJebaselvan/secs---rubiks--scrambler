# secs---rubiks--scrambler
Aerohack Project Files 
# 🧠 SECS++: Heuristic-Based Rubik's Cube Solver

Welcome to the **SECS++ Rubik's Cube Solver** — an intelligent, phase-based, heuristic-driven solution built using Python.  
This solver models human-style solving by operating in **three logical stages**:
- **Cross**
- **First Two Layers (F2L)**
- **Last Layer (LL)**

It uses a heuristic beam search and flat-dictionary cube representation for performance and clarity.

---

## ✈️ Built for AeroHack 2025

Developed for the **Design Challenge Round** of *Collins Aerospace AeroHack 2025*, SECS++ simulates cognitive problem solving.  
The system is optimized for integration into autonomous agents such as drones and manipulators where state-driven decision-making is essential.

---

## 🔧 Features

- ✅ Flat-dictionary Rubik’s Cube representation
- 🔁 3-Phase Solving: CROSS → F2L → LAST
- 🧠 Entropy-based and misalignment heuristic
- 🔍 Beam Search-based decision tree (SECS++ V5.1)
- 🧪 Validated with random and manual scrambles
- 📦 Modular and easy to extend

---

## 📐 Algorithm Summary

### Phase-Based Looping
Each solving phase is looped until the heuristic-based goal is reached.  
For each candidate move, the solver evaluates a cost:
---

### 🎯 Cost Function (SECS++ Heuristic)
```math
F(n) = a ⋅ H_{diff}(n) + b ⋅ E(n)

```

Where:

H_diff(n) = Number of misplaced stickers

E(n) = Entropy (color variation per face)

a, b = Phase-specific weights

---
🧪 Sample Output

=== Scramble: ['U2', "F'", 'U', 'F2', 'D', 'F2']

--- Scrambled Cube State ---
U: ['U', 'U', 'F', ...]
D: ['D', 'D', 'D', ...]
...

=== PHASE: CROSS ===
=== PHASE: F2L ===
=== PHASE: LAST ===

✅ Solved Cube State:
U: ['U', 'U', 'U', ..., 'U']
D: ['D', 'D', 'D', ..., 'D']
...

Moves to solve: ['U', 'F', 'R2', ...]
---

📁 Folder Structure
bash
Copy
Edit
secs_cube_solver/
├── app.py                       # Main executable
├── requirements.txt             # Package dependencies
├── README.md                    # Project info (this file)
└── secs/
    ├── __init__.py
    ├── cube_state.py            # Cube state model
    ├── moves.py                 # All cube moves
    ├── utils.py                 # Utilities: printer, heuristic, checker
    ├── cost.py                  # Cost evaluation
    ├── solver.py                # SECS++ core logic
    └── looped_phased_solver.py # 3-phase control logic

---

🌟 Future Additions
Real-time camera input for color-based scrambling

Integration with drone & robotic simulation

Advanced SECS++ with parallel beam search

Web-based visualization of solving path
---

📚 Requirements
Python 3.7+

NumPy
---
🧠 Author
P. Jeba Selvan Andrew
GitHub Profile

---

