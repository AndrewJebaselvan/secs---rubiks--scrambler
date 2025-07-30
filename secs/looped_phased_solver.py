from secs.solver import secs_solve
from secs.utils import is_cube_solved, print_cube
from secs.moves import apply_move_to_state  # ✅ Fix: Added missing import

def looped_phased_solve(initial_state):
    current_state = initial_state.copy()
    total_moves = []

    phases = [
        {"phase": "cross", "config": {"phase": "cross", "alpha": 1.0, "beta": 0.5, "delta": 2.0}},
        {"phase": "f2l", "config": {"phase": "f2l", "alpha": 1.0, "beta": 0.5, "delta": 2.0}},
        {"phase": "last", "config": {"phase": "last", "alpha": 1.0, "beta": 0.5, "delta": 2.0}},
    ]

    for phase in phases:
        print(f"\n=== PHASE: {phase['phase'].upper()} ===")
        while not is_cube_solved(current_state["cube"]):
            result = secs_solve(current_state, phase["config"])
            for move in result:
                current_state["cube"] = apply_move_to_state(current_state, move)
            total_moves.extend(result)
            break

    print("\n✅ Solved Cube State:")
    print_cube(current_state["cube"])
    return total_moves
