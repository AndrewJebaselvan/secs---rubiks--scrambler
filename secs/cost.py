# cost.py

def _calculate_h_diff(cube_state):
    """
    Calculates the Misalignment Heuristic (H_diff).
    This counts the total number of stickers on all faces that do not
    match the color of their face's center sticker.
    H_diff(n) = Σ(face) Σ(i=0 to 8) [face_i ≠ face_4]
    """
    h_diff_cost = 0
    for face in "UDFBLR":
        center_sticker_color = cube_state[f"{face}4"]
        for i in range(9):
            if cube_state[f"{face}{i}"] != center_sticker_color:
                h_diff_cost += 1
    return h_diff_cost

def _calculate_entropy(cube_state):
    """
    Calculates the Entropy Heuristic (E).
    This measures the color diversity on each face. For each face, it counts
    the number of unique colors present and sums these counts. A lower
    entropy score means the faces are more monochromatic and thus closer to solved.
    E(n) = Σ(face) |unique(face_0...face_8)|
    """
    entropy_cost = 0
    for face in "UDFBLR":
        face_stickers = [cube_state[f"{face}{i}"] for i in range(9)]
        # The number of unique colors on the face is the size of the set of sticker colors
        entropy_cost += len(set(face_stickers))
    return entropy_cost

def compute_cost(cube_state, config):
    """
    Computes the main heuristic function cubeeval(n) based on the solving phase.
    cubeeval(n) = a * H_diff(n) + b * E(n)
    """
    phase = config.get("phase", "cross")

    # Define the phase-specific weights for a and b from your documentation
    weights = {
        "cross":      {"a": 1.0, "b": 0.5},
        "f2l":        {"a": 1.5, "b": 1.0},
        "last_layer": {"a": 1.0, "b": 2.0}
    }
    
    a = weights[phase]["a"]
    b = weights[phase]["b"]

    # Calculate the two heuristic components
    h_diff = _calculate_h_diff(cube_state)
    entropy = _calculate_entropy(cube_state)

    # Return the final weighted heuristic cost
    total_cost = (a * h_diff) + (b * entropy)
    return total_cost
