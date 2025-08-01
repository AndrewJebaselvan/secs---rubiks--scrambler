

from .solver import secs_solve
from .moves import apply_move_to_state
from .cube_state import CubeState

def looped_phased_solve(initial_state):


    current_state = initial_state.copy()
    move_history = []

    print("\n🔵 Phase 1: Solving Cross...")
    cross_config = {
        "phase": "cross",
        "max_steps": 20, 
        "beam_width": 20
    }
    cross_moves = secs_solve(current_state, cross_config)
    move_history.extend(cross_moves)
    
    for move in cross_moves:
        current_state["cube"] = apply_move_to_state(current_state["cube"], move)
    
    print(f"--- Cross solved with {len(cross_moves)} moves: {' '.join(cross_moves)} ---")


    print("\n🟢 Phase 2: Solving F2L...")

    f2l_config = {
        "phase": "f2l",
        "max_steps": 100,
        "beam_width": 100
    }
    f2l_moves = secs_solve(current_state, f2l_config)
    move_history.extend(f2l_moves)

    for move in f2l_moves:
        current_state["cube"] = apply_move_to_state(current_state["cube"], move)
        
    print(f"--- F2L solved with {len(f2l_moves)} moves: {' '.join(f2l_moves)} ---")


    print("\n🟣 Phase 3: Solving Last Layer...")

    last_layer_config = {
        "phase": "last_layer",
        "max_steps": 120,
        "beam_width": 120
    }
    last_layer_moves = secs_solve(current_state, last_layer_config)
    move_history.extend(last_layer_moves)
    
    for move in last_layer_moves:
         current_state["cube"] = apply_move_to_state(current_state["cube"], move)

    print(f"--- Last Layer solved with {len(last_layer_moves)} moves: {' '.join(last_layer_moves)} ---")


    print(f"\n✅ Cube Solved in {len(move_history)} moves!")
    return move_history
