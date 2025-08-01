# solver.py
from .moves import apply_move_to_state
from .utils import default_candidate_moves, goal_reached
from .cost import compute_cost 
from .cube_state import CubeState

def secs_solve(initial_state, config):

    cube_dict = initial_state["cube"]
    phase = config.get("phase", "cross")
    max_steps = config.get("max_steps", 10)
    beam_width = config.get("beam_width", 5) 

    if goal_reached(initial_state, phase):
        print(f"Phase '{phase}' is already solved.")
        return []

    h_cost = compute_cost(cube_dict, config) 
    g_cost = 0 
    queue = [{
        "cube": cube_dict,
        "moves": [],
        "cost": h_cost + g_cost
    }]
    

    visited = {str(sorted(cube_dict.items())): 0}

    for i in range(max_steps):
        next_queue = []
        for node in queue:
            for move in default_candidate_moves():
                new_cube_dict = apply_move_to_state(node["cube"], move)

                state_key = str(sorted(new_cube_dict.items()))
                path_len = len(node["moves"]) + 1
                if state_key in visited and visited[state_key] <= path_len:
                    continue
                visited[state_key] = path_len
                h_cost = compute_cost(new_cube_dict, config)
                g_cost = path_len
                total_cost = h_cost + g_cost
                
                next_queue.append({
                    "cube": new_cube_dict,
                    "moves": node["moves"] + [move],
                    "cost": total_cost
                })
        
        if not next_queue:
            print(f"Search ended early for phase '{phase}': no new states to explore.")
            break
        queue = sorted(next_queue, key=lambda x: x["cost"])[:beam_width]
        for candidate in queue:
            if goal_reached(candidate, phase):
                print(f"Phase '{phase}' goal reached!")
                return candidate["moves"]
                
    print(f"Phase '{phase}' did not reach goal, returning best effort.")
    return queue[0]["moves"]
