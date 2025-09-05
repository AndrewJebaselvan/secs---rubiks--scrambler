import random
from secs.cube_state import CubeState

def default_candidate_moves():
    """Returns a list of all 18 possible moves."""
    return [
        "U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", 
        "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2"
    ]

def goal_reached(state, phase):
    """Checks if the cube has reached the goal state for a given phase."""
    cube = state["cube"]
    goal_cube = CubeState().get_solved_state()

    if phase == 'cross_solved':
        # Check if the Down-face cross edges are solved and oriented
        return (cube['D1'] == 'D' and cube['F7'] == 'F' and
                cube['D3'] == 'D' and cube['L7'] == 'L' and
                cube['D5'] == 'D' and cube['R7'] == 'R' and
                cube['D7'] == 'D' and cube['B7'] == 'B')

    if phase == 'f2l':
        # Check if the first two layers (Down face and middle layer) are solved
        f2l_pieces = [k for k in goal_cube.keys() if k.startswith('D') or k[1] in '345']
        return all(cube.get(piece) == goal_cube.get(piece) for piece in f2l_pieces)
    
    if phase == 'last_layer':
        # Check if the entire cube is solved
        return all(cube.get(k) == v for k, v in goal_cube.items())
    
    return False

def generate_scramble(n=20):
    """Generates a random scramble of a given length."""
    return [random.choice(default_candidate_moves()) for _ in range(n)]

def dict_to_cubestring(state_dict):
    """Converts our flat dictionary format to the Kociemba solver's string format."""
    # Kociemba's order is URFDLB
    order = {
        'U': [f'U{i}' for i in range(9)], 'R': [f'R{i}' for i in range(9)],
        'F': [f'F{i}' for i in range(9)], 'D': [f'D{i}' for i in range(9)],
        'L': [f'L{i}' for i in range(9)], 'B': [f'B{i}' for i in range(9)],
    }
    cubestring = ""
    for face in "URFDLB":
        for sticker_key in order[face]:
            cubestring += state_dict.get(sticker_key, '?')
    return cubestring

def cubestring_to_dict(cubestring):
    """Converts the Kociemba solver's string format to our flat dictionary format."""
    if len(cubestring) != 54:
        raise ValueError("Cubestring must be 54 characters long")
    
    state_dict = {}
    order = "URFDLB"
    for i, face in enumerate(order):
        for j in range(9):
            state_dict[f'{face}{j}'] = cubestring[i*9 + j]
    return state_dict

