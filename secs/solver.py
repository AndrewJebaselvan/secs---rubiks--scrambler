from .moves import apply_move_to_state
from .utils import default_candidate_moves, goal_reached
from .cost import compute_cost # This will be our implementation of cubeeval(n)
from .cube_state import CubeState

def secs_solve(initial_state, config):
    """
    Performs an A* Search using a custom heuristic function to find a solution.

    The total cost is f(n) = g(n) + h(n), where:
    - g(n) is the number of moves made (path length).
    - h(n) is the custom heuristic from cost.py (cubeeval).
    """
    cube_dict = initial_state["cube"]
    phase = config.get("phase", "cross")
    max_steps = config.get("max_steps", 100) # Increased default for more power
    beam_width = config.get("beam_width", 100) # Increased default for a wider search

    # Check if the phase is already solved before starting the search
    if goal_reached(initial_state, phase):
        print(f"Phase '{phase}' is already solved.")
        return []

    # The queue holds the "beam" of the best states found so far.
    # The cost is calculated using the combined A* formula.
    h_cost = compute_cost(cube_dict, config) # Your custom cubeeval(n)
    g_cost = 0 # Path length starts at 0
    queue = [{
        "cube": cube_dict,
        "moves": [],
        "cost": h_cost + g_cost
    }]
    
    # Keep track of visited states to avoid simple cycles and redundant work.
    # The key is a string representation of the cube state.
    # The value is the length of the shortest path found so far to that state.
    visited = {str(sorted(cube_dict.items())): 0}

    for i in range(max_steps):
        next_queue = []
        for node in queue:
            for move in default_candidate_moves():
                new_cube_dict = apply_move_to_state(node["cube"], move)
                
                path_len = len(node["moves"]) + 1
                state_key = str(sorted(new_cube_dict.items()))
                
                # If we've seen this state before via a shorter or equal path, skip it.
                if state_key in visited and visited[state_key] <= path_len:
                    continue
                
                visited[state_key] = path_len

                # Calculate the A* cost using your custom function as the heuristic h(n)
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

        # This is the core of the Beam Search aspect of our A*:
        # Sort all potential next states by the combined A* cost and keep only the
        # top 'k' (the beam_width) states for the next iteration.
        queue = sorted(next_queue, key=lambda x: x["cost"])[:beam_width]

        # Check if any of the top candidates in the beam have reached the goal
        for candidate in queue:
            if goal_reached(candidate, phase):
                print(f"Phase '{phase}' goal reached!")
                return candidate["moves"]
                
    print(f"Phase '{phase}' did not reach goal, returning best effort.")
    # If no solution is found, return the moves from the best state we discovered
    return queue[0]["moves"]
