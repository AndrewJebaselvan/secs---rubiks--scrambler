

def _calculate_h_diff(cube_state):

    h_diff_cost = 0
    for face in "UDFBLR":
        center_sticker_color = cube_state[f"{face}4"]
        for i in range(9):
            if cube_state[f"{face}{i}"] != center_sticker_color:
                h_diff_cost += 1
    return h_diff_cost

def _calculate_entropy(cube_state):

    entropy_cost = 0
    for face in "UDFBLR":
        face_stickers = [cube_state[f"{face}{i}"] for i in range(9)]

        entropy_cost += len(set(face_stickers))
    return entropy_cost

def compute_cost(cube_state, config):

    phase = config.get("phase", "cross")

    weights = {
        "cross":      {"a": 1.0, "b": 0.5},
        "f2l":        {"a": 1.5, "b": 1.0},
        "last_layer": {"a": 1.0, "b": 2.0}
    }
    
    a = weights[phase]["a"]
    b = weights[phase]["b"]

    h_diff = _calculate_h_diff(cube_state)
    entropy = _calculate_entropy(cube_state)

    total_cost = (a * h_diff) + (b * entropy)
    return total_cost
