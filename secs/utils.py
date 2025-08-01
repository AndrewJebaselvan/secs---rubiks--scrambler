
import random
from secs.moves import apply_move_to_state
from secs.cube_state import CubeState


def default_candidate_moves():

    return ["U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", 
            "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2"]

def goal_reached(state, phase):

    cube = state["cube"]
    goal_cube = CubeState().get_solved_state() 

    phase = phase.lower() 

    if phase == "cross":

        cross_stickers = ['D1', 'D3', 'D5', 'D7', 'F7', 'L7', 'R7', 'B7']
        for sticker in cross_stickers:
            if cube.get(sticker) != goal_cube.get(sticker):
                return False
        return True

    if phase == "f2l":

        first_two_layers_stickers = [
            'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
            'F3', 'F5', 'F6', 'F8', 'R3', 'R5', 'R6', 'R8',
            'B3', 'B5', 'B6', 'B8', 'L3', 'L5', 'L6', 'L8'
        ]
        for sticker in first_two_layers_stickers:
            if cube.get(sticker) != goal_cube.get(sticker):
                return False
        return True
        
    if phase == "last_layer":

        for sticker_key in goal_cube:
            if cube.get(sticker_key) != goal_cube.get(sticker_key):
                return False
        return True

    return False


def apply_scramble(cube_state, moves):
    """Applies a series of moves to a CubeState object."""
    current_cube_dict = dict(cube_state.state)
    for move in moves:
        current_cube_dict = apply_move_to_state(current_cube_dict, move)
    return {"cube": current_cube_dict}

def generate_scramble(n=15):
    """Generates a random scramble sequence."""
    return [random.choice(default_candidate_moves()) for _ in range(n)]
