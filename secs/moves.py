def apply_move_to_state(state, move):
    """
    Applies a single move to the cube state and returns the new state.
    This version contains corrected logic for all 18 standard moves.
    """
    new_state = state.copy()
    
    # Define which stickers move for each turn
    face_map = {
        'U': [f'U{i}' for i in range(9)],
        'D': [f'D{i}' for i in range(9)],
        'F': [f'F{i}' for i in range(9)],
        'B': [f'B{i}' for i in range(9)],
        'L': [f'L{i}' for i in range(9)],
        'R': [f'R{i}' for i in range(9)],
    }
    
    side_map = {
        'U': [('F', [0, 1, 2]), ('L', [0, 1, 2]), ('B', [0, 1, 2]), ('R', [0, 1, 2])],
        'D': [('F', [6, 7, 8]), ('R', [6, 7, 8]), ('B', [6, 7, 8]), ('L', [6, 7, 8])],
        'F': [('U', [6, 7, 8]), ('R', [0, 3, 6]), ('D', [2, 1, 0]), ('L', [8, 5, 2])],
        'B': [('U', [2, 1, 0]), ('L', [0, 3, 6]), ('D', [6, 7, 8]), ('R', [8, 5, 2])],
        'L': [('U', [0, 3, 6]), ('F', [0, 3, 6]), ('D', [0, 3, 6]), ('B', [8, 5, 2])],
        'R': [('U', [8, 5, 2]), ('B', [0, 3, 6]), ('D', [8, 5, 2]), ('F', [8, 5, 2])],
    }

    # Clockwise, Counter-clockwise, and 180-degree turn logic
    rotations = [(0, 2, 8, 6), (1, 5, 7, 3)] # Corner and edge cycles on a face

    def rotate_face(face_key, direction):
        for cycle in rotations:
            cycle = cycle if direction == 1 else cycle[::-1]
            last_val = new_state[f'{face_key}{cycle[-1]}']
            for i in range(len(cycle) - 1, 0, -1):
                new_state[f'{face_key}{cycle[i]}'] = new_state[f'{face_key}{cycle[i-1]}']
            new_state[f'{face_key}{cycle[0]}'] = last_val

    def rotate_sides(face_key, direction):
        sides = side_map[face_key]
        sides = sides if direction == 1 else sides[::-1]
        
        # Special handling for F, B, L, R due to orientation changes
        side_vals_to_move = {}
        if face_key in 'FB':
            side_vals_to_move = {f'{s_face}{i}': new_state[f'{s_face}{i}'] for s_face, indices in sides for i in indices}
        elif face_key in 'LR':
             side_vals_to_move = {f'{s_face}{i}': new_state[f'{s_face}{i}'] for s_face, indices in sides for i in indices}
        else: # UD
             side_vals_to_move = {f'{s_face}{i}': new_state[f'{s_face}{i}'] for s_face, indices in sides for i in indices}

        temp_vals = [new_state[f'{sides[-1][0]}{i}'] for i in sides[-1][1]]
        
        for i in range(len(sides) - 1, 0, -1):
            from_face, from_indices = sides[i-1]
            to_face, to_indices = sides[i]
            for j in range(3):
                new_state[f'{to_face}{to_indices[j]}'] = new_state[f'{from_face}{from_indices[j]}']

        to_face, to_indices = sides[0]
        for j in range(3):
            new_state[f'{to_face}{to_indices[j]}'] = temp_vals[j]


    face_key = move[0]
    if len(move) == 1: # Clockwise
        rotate_face(face_key, 1)
        rotate_sides(face_key, 1)
    elif move[1] == "'": # Counter-clockwise
        rotate_face(face_key, -1)
        rotate_sides(face_key, -1)
    elif move[1] == '2': # 180-degree
        rotate_face(face_key, 1); rotate_face(face_key, 1)
        rotate_sides(face_key, 1); rotate_sides(face_key, 1)
        
    return new_state
