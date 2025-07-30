from secs.utils import heuristic_diff, entropy_scalar, count_cross_edges, count_f2l_pairs, count_solved_faces

def compute_cost(state, config):
    cube = state["cube"]
    phase = config.get("phase", "")
    h = heuristic_diff(cube)
    e = entropy_scalar(cube)

    bonus = 0
    if phase == "cross":
        bonus = min(count_cross_edges(cube) * 3, 12)
    elif phase == "f2l":
        bonus = min(count_f2l_pairs(cube) * 5, 20)
    elif phase == "last":
        bonus = min(count_solved_faces(cube) * 10, 60)

    alpha = config.get("alpha", 1.0)
    beta = config.get("beta", 0.5)
    delta = config.get("delta", 2.0)

    return alpha * h + beta * e - delta * bonus
