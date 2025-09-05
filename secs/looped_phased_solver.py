import kociemba
from .solver import secs_solve
from .moves import apply_move_to_state
from .utils import goal_reached

def looped_phased_solve(initial_state, initial_cubestring):
    """
    Solves the cube using a hybrid strategy:
    1. Attempts to solve with the A* search and custom heuristic.
    2. If the A* search fails at any phase, it engages Kociemba's algorithm as a failover.
    """
    current_state = initial_state.copy()
    move_history = []


    print("\n🔵 Phase 1: Solving Cross with A* Search...")
    cross_config = {"phase": "cross", "max_steps": 30, "beam_width": 30}
    cross_moves = secs_solve(current_state, cross_config)
    
    for move in cross_moves:
        current_state['cube'] = apply_move_to_state(current_state['cube'], move)
    
    if not goal_reached(current_state, 'cross'):
        print("\n⚠️ A* search failed to solve the Cross. Engaging Kociemba solver...")
        kociemba_solution = kociemba.solve(initial_cubestring)
        return kociemba_solution
    
    move_history.extend(cross_moves)
    print(f"--- Cross solved with {len(cross_moves)} moves. ---")


    print("\n🟢 Phase 2: Solving F2L with A* Search...")
    f2l_config = {"phase": "f2l", "max_steps": 60, "beam_width": 60}
    f2l_moves = secs_solve(current_state, f2l_config)
    
    for move in f2l_moves:
        current_state['cube'] = apply_move_to_state(current_state['cube'], move)

    if not goal_reached(current_state, 'f2l'):
        print("\n⚠️ A* search failed to solve F2L. Engaging Kociemba solver...")
        kociemba_solution = kociemba.solve(initial_cubestring)
        return kociemba_solution
        
    move_history.extend(f2l_moves)
    print(f"--- F2L solved with {len(f2l_moves)} moves. ---")
    

    print("\n🟣 Phase 3: Solving Last Layer with A* Search...")
    last_layer_config = {"phase": "last_layer", "max_steps": 80, "beam_width": 80}
    last_layer_moves = secs_solve(current_state, last_layer_config)
    
    for move in last_layer_moves:
        current_state["cube"] = apply_move_to_state(current_state["cube"], move)
    
    if not goal_reached(current_state, 'last_layer'):
        print("\n⚠️ A* search failed to solve Last Layer. Engaging Kociemba solver...")
        kociemba_solution = kociemba.solve(initial_cubestring)
        return kociemba_solution

    move_history.extend(last_layer_moves)
    print(f"--- Last Layer solved with {len(last_layer_moves)} moves. ---")

    print(f"\n✅ Cube Solved in {len(move_history)} moves!")
    return move_history
