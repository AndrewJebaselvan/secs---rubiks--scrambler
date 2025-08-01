🧠 SECS++: Heuristic-Based Rubik's Cube Solver
Welcome to the SECS++ Rubik's Cube Solver — an intelligent, phase-based, heuristic-driven solution built using Python. This solver models human-style solving by operating in three logical stages: Cross, First Two Layers (F2L), and Last Layer (LL).

It uses a powerful A* (A-star) search algorithm guided by a unique, custom-designed heuristic to find efficient solutions to complex scrambles.

✈️ Built for AeroHack 2025
Developed for the Design Challenge Round of Collins Aerospace AeroHack 2025, SECS++ simulates cognitive problem-solving. The system is optimized for integration into autonomous agents such as drones and manipulators where state-driven decision-making is essential.

🔧 Features
✅ Flat-dictionary Cube Representation: Fast and efficient state management.
✅ 3-Phase Solving: Logically breaks down the problem into CROSS → F2L → LAST LAYER.
✅ Custom Heuristic Function: A unique cost function combining sticker misalignment and facial entropy.
✅ *A Search Algorithm:** An intelligent search that balances solution length with heuristic guidance.
✅ Validated: Tested with random and manual scrambles, achieving full solves.
✅ Modular and Extensible: Code is organized for clarity and future development.

📐 Algorithm Summary
The solver uses a phased approach, applying a powerful A* search algorithm to solve each stage of the cube.

A* Search Logic
The core of the solver is the A* search, which finds the best path by minimizing a cost function f(n) for each cube state n:

f(n) = g(n) + h(n)

Where:

g(n) = The number of moves already taken (the path cost).

h(n) = The estimated cost to the goal, provided by our custom heuristic.

This ensures the solver finds a balance between a short solution and making progress.

🎯 The Custom Heuristic: h(n)
Our "secret sauce" is the custom heuristic function that guides the A* search. It is a weighted sum of two metrics:

h(n) = a · H_diff(n) + b · E(n)

Where:

H_diff(n) = The Misalignment Heuristic (number of misplaced stickers).

E(n) = The Entropy Heuristic (a measure of color disorder on each face).

a, b = Phase-specific weights that tune the solver's focus.

🧪 Sample Output
$ python app.py
Enter scramble moves separated by space (or press Enter for random scramble): R U R' U R U2 R' U

=== Scramble: R U R' U R U2 R' U ===

--- Scrambled Cube State ---
U: ['U', 'U', 'B', 'U', 'U', 'U', 'L', 'U', 'R']
...

🔵 Phase 1: Solving Cross...
Phase 'cross' is already solved.
--- Cross solved with 0 moves: ---

🟢 Phase 2: Solving F2L...
Phase 'f2l' goal reached!
--- F2L solved with 8 moves: U' R U2 R' U' R U' R' ---

🟣 Phase 3: Solving Last Layer...
Phase 'last_layer' is already solved.
--- Last Layer solved with 0 moves: ---

✅ Cube Solved in 8 moves!

=== SOLUTION FOUND ===
Solved in 8 moves:
U' R U2 R' U' R U' R'

📁 Folder Structure
secs_cube_solver/
├── app.py                  # Main executable
├── README.md               # Project info (this file)
└── secs/
    ├── __init__.py
    ├── cube_state.py       # Cube state model
    ├── moves.py            # All cube moves
    ├── utils.py            # Utilities and goal checker
    ├── cost.py             # Custom heuristic cost function
    ├── solver.py           # A* search algorithm logic
    └── looped_phased_solver.py # 3-phase control logic

🌟 Future Additions
Real-time camera input for color-based scrambling.

Integration with drone & robotic simulation environments.

Web-based visualization of the solving path.

🧠 Author
P. Jeba Selvan Andrew

GitHub Profile
