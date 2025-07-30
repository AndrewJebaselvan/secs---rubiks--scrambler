# moves.py — Flat dictionary-based Rubik's Cube move logic

import copy

FACE_NAMES = ["U", "D", "F", "B", "L", "R"]

# Define flat indices for each face
FACE_INDICES = {
    "U": [f"U{i}" for i in range(9)],
    "D": [f"D{i}" for i in range(9)],
    "F": [f"F{i}" for i in range(9)],
    "B": [f"B{i}" for i in range(9)],
    "L": [f"L{i}" for i in range(9)],
    "R": [f"R{i}" for i in range(9)],
}

# Moves list for solving and scrambling
MOVES = [f + suf for f in FACE_NAMES for suf in ["", "'", "2"]]

def default_candidate_moves():
    return MOVES.copy()

def copy_flat_cube(cube):
    return {k: v for k, v in cube.items()}

def invert_move(move):
    if len(move) == 1:
        return move + "'"
    elif move[1] == "'":
        return move[0]
    else:
        return move  # "2" stays "2"

def normalize_move(move):
    return move.strip().upper()

# Basic 90-degree clockwise face rotation
def rotate_face(face):
    return [
        face[6], face[3], face[0],
        face[7], face[4], face[1],
        face[8], face[5], face[2]
    ]

# Basic 90-degree counter-clockwise face rotation
def rotate_face_ccw(face):
    return [
        face[2], face[5], face[8],
        face[1], face[4], face[7],
        face[0], face[3], face[6]
    ]

# Apply move to flat cube dictionary
def apply_move_to_state(state_dict, move):
    cube = copy_flat_cube(state_dict["cube"])
    face = move[0]
    times = 1 if len(move) == 1 else (2 if move[1] == "2" else 3)

    for _ in range(times):
        apply_single_face_rotation(cube, face)

    return {"cube": cube}  # ✅ Return wrapped in {"cube": ...}


# Applies only face rotation for now
def apply_single_face_rotation(cube, face):
    face_indices = FACE_INDICES[face]
    face_values = [cube[idx] for idx in face_indices]
    rotated = rotate_face(face_values)
    for idx, val in zip(face_indices, rotated):
        cube[idx] = val
    # NOTE: Adjacent edge rotation not yet implemented (simplified version)
