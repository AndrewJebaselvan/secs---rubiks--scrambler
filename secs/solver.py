from secs.moves import apply_move_to_state
from secs.utils import default_candidate_moves, goal_reached
from secs.cost import compute_cost

def secs_solve(initial_state, config):
    cube = initial_state["cube"]
    max_steps = config.get("max_steps", 10)
    beam_width = config.get("beam_width", 5)

    queue = [{"cube": cube, "moves": [], "cost": compute_cost(initial_state, config)}]

    for _ in range(max_steps):
        next_queue = []
        for node in queue:
            for move in default_candidate_moves():
                new_cube = apply_move_to_state(node, move)
                new_state = {"cube": new_cube}
                cost = compute_cost(new_state, config)
                next_queue.append({
                    "cube": new_cube,
                    "moves": node["moves"] + [move],
                    "cost": cost
                })

        queue = sorted(next_queue, key=lambda x: x["cost"])[:beam_width]

        for candidate in queue:
            if goal_reached(candidate, config.get("phase", "")):
                return candidate["moves"]
    return queue[0]["moves"]
