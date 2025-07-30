import random

FACES = ['U', 'D', 'F', 'B', 'L', 'R']
MOVES = [f + suf for f in FACES for suf in ['', "'", '2']]

def default_candidate_moves():
    return MOVES.copy()

def print_cube(flat_cube):
    for face in FACES:
        face_values = [flat_cube[f"{face}{i}"] for i in range(9)]
        print(f"{face}: {face_values}")

def generate_scramble(n=6):
    return [random.choice(MOVES) for _ in range(n)]

def apply_scramble(cube, scramble, apply_move_func):
    for move in scramble:
        cube.state = apply_move_func({"cube": cube.state}, move)["cube"]
    return cube


def is_cube_solved(cube):
    for face in FACES:
        center = cube[f"{face}4"]
        if not all(cube[f"{face}{i}"] == center for i in range(9)):
            return False
    return True

def goal_reached(state, phase):
    cube = state["cube"]
    if phase == "cross":
        return count_cross_edges(cube) == 4
    elif phase == "f2l":
        return count_f2l_pairs(cube) == 4
    elif phase == "last":
        return count_solved_faces(cube) >= 6
    else:
        return is_cube_solved(cube)

def heuristic_diff(cube):
    count = 0
    for face in FACES:
        center = cube[f"{face}4"]
        count += sum(1 for i in range(9) if cube[f"{face}{i}"] != center)
    return count

def entropy_scalar(cube):
    return sum(len(set(cube[f"{face}{i}"] for i in range(9))) for face in FACES)

def count_cross_edges(cube):
    center = cube["U4"]
    indices = ["U1", "U3", "U5", "U7"]
    return sum(1 for idx in indices if cube[idx] == center)

def count_f2l_pairs(cube):
    return sum(1 for f in ['F', 'R', 'L', 'B'] if cube[f + '6'] == cube[f + '4'])

def count_solved_faces(cube):
    return sum(
        all(cube[f"{face}{i}"] == cube[f"{face}4"] for i in range(9))
        for face in FACES
    )
