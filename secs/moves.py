

def _rotate_face_clockwise(state, face):

    stickers = [f"{face}{i}" for i in range(9)]
    
    temp = state[stickers[0]]
    state[stickers[0]] = state[stickers[6]]
    state[stickers[6]] = state[stickers[8]]
    state[stickers[8]] = state[stickers[2]]
    state[stickers[2]] = temp

    temp = state[stickers[1]]
    state[stickers[1]] = state[stickers[3]]
    state[stickers[3]] = state[stickers[7]]
    state[stickers[7]] = state[stickers[5]]
    state[stickers[5]] = temp
    return state

def _rotate_face_counter_clockwise(state, face):

    stickers = [f"{face}{i}" for i in range(9)]

    temp = state[stickers[0]]
    state[stickers[0]] = state[stickers[2]]
    state[stickers[2]] = state[stickers[8]]
    state[stickers[8]] = state[stickers[6]]
    state[stickers[6]] = temp

    temp = state[stickers[1]]
    state[stickers[1]] = state[stickers[5]]
    state[stickers[5]] = state[stickers[7]]
    state[stickers[7]] = state[stickers[3]]
    state[stickers[3]] = temp
    return state


def apply_move_to_state(state, move):

    new_state = state.copy()

    U_adj = {"F": ["F0", "F1", "F2"], "R": ["R0", "R1", "R2"], "B": ["B0", "B1", "B2"], "L": ["L0", "L1", "L2"]}
    D_adj = {"F": ["F6", "F7", "F8"], "L": ["L6", "L7", "L8"], "B": ["B6", "B7", "B8"], "R": ["R6", "R7", "R8"]}
    L_adj = {"U": ["U0", "U3", "U6"], "B": ["B2", "B5", "B8"], "D": ["D0", "D3", "D6"], "F": ["F0", "F3", "F6"]}
    R_adj = {"U": ["U2", "U5", "U8"], "F": ["F2", "F5", "F8"], "D": ["D2", "D5", "D8"], "B": ["B0", "B3", "B6"]}
    F_adj = {"U": ["U6", "U7", "U8"], "L": ["L2", "L5", "L8"], "D": ["D0", "D1", "D2"], "R": ["R0", "R3", "R6"]}
    B_adj = {"U": ["U0", "U1", "U2"], "R": ["R2", "R5", "R8"], "D": ["D6", "D7", "D8"], "L": ["L0", "L3", "L6"]}

    if move == "U":
        _rotate_face_clockwise(new_state, "U")
        temp = {s: new_state[s] for s in U_adj["F"]}
        for i in range(3): new_state[U_adj["F"][i]] = new_state[U_adj["L"][i]]
        for i in range(3): new_state[U_adj["L"][i]] = new_state[U_adj["B"][i]]
        for i in range(3): new_state[U_adj["B"][i]] = new_state[U_adj["R"][i]]
        for i in range(3): new_state[U_adj["R"][i]] = temp[U_adj["F"][i]]
    
    elif move == "U'":
        _rotate_face_counter_clockwise(new_state, "U")
        temp = {s: new_state[s] for s in U_adj["F"]}
        for i in range(3): new_state[U_adj["F"][i]] = new_state[U_adj["R"][i]]
        for i in range(3): new_state[U_adj["R"][i]] = new_state[U_adj["B"][i]]
        for i in range(3): new_state[U_adj["B"][i]] = new_state[U_adj["L"][i]]
        for i in range(3): new_state[U_adj["L"][i]] = temp[U_adj["F"][i]]

    elif move == "D":
        _rotate_face_clockwise(new_state, "D")
        temp = {s: new_state[s] for s in D_adj["F"]}
        for i in range(3): new_state[D_adj["F"][i]] = new_state[D_adj["R"][i]]
        for i in range(3): new_state[D_adj["R"][i]] = new_state[D_adj["B"][i]]
        for i in range(3): new_state[D_adj["B"][i]] = new_state[D_adj["L"][i]]
        for i in range(3): new_state[D_adj["L"][i]] = temp[D_adj["F"][i]]

    elif move == "D'":
        _rotate_face_counter_clockwise(new_state, "D")
        temp = {s: new_state[s] for s in D_adj["F"]}
        for i in range(3): new_state[D_adj["F"][i]] = new_state[D_adj["L"][i]]
        for i in range(3): new_state[D_adj["L"][i]] = new_state[D_adj["B"][i]]
        for i in range(3): new_state[D_adj["B"][i]] = new_state[D_adj["R"][i]]
        for i in range(3): new_state[D_adj["R"][i]] = temp[D_adj["F"][i]]

    elif move == "L":
        _rotate_face_clockwise(new_state, "L")
        temp = {s: new_state[s] for s in L_adj["U"]}
        for i in range(3): new_state[L_adj["U"][i]] = new_state[L_adj["F"][i]]
        for i in range(3): new_state[L_adj["F"][i]] = new_state[L_adj["D"][i]]
        for i in range(3): new_state[L_adj["D"][i]] = new_state[L_adj["B"][i]]
        for i in range(3): new_state[L_adj["B"][i]] = temp[L_adj["U"][i]]

    elif move == "L'":
        _rotate_face_counter_clockwise(new_state, "L")
        temp = {s: new_state[s] for s in L_adj["U"]}
        for i in range(3): new_state[L_adj["U"][i]] = new_state[L_adj["B"][i]]
        for i in range(3): new_state[L_adj["B"][i]] = new_state[L_adj["D"][i]]
        for i in range(3): new_state[L_adj["D"][i]] = new_state[L_adj["F"][i]]
        for i in range(3): new_state[L_adj["F"][i]] = temp[L_adj["U"][i]]

    elif move == "R":
        _rotate_face_clockwise(new_state, "R")
        temp = {s: new_state[s] for s in R_adj["U"]}
        for i in range(3): new_state[R_adj["U"][i]] = new_state[R_adj["B"][i]]
        for i in range(3): new_state[R_adj["B"][i]] = new_state[R_adj["D"][i]]
        for i in range(3): new_state[R_adj["D"][i]] = new_state[R_adj["F"][i]]
        for i in range(3): new_state[R_adj["F"][i]] = temp[R_adj["U"][i]]

    elif move == "R'":
        _rotate_face_counter_clockwise(new_state, "R")
        temp = {s: new_state[s] for s in R_adj["U"]}
        for i in range(3): new_state[R_adj["U"][i]] = new_state[R_adj["F"][i]]
        for i in range(3): new_state[R_adj["F"][i]] = new_state[R_adj["D"][i]]
        for i in range(3): new_state[R_adj["D"][i]] = new_state[R_adj["B"][i]]
        for i in range(3): new_state[R_adj["B"][i]] = temp[R_adj["U"][i]]

    elif move == "F":
        _rotate_face_clockwise(new_state, "F")
        temp = {s: new_state[s] for s in F_adj["U"]}
        for i in range(3): new_state[F_adj["U"][i]] = new_state[F_adj["L"][i]]
        for i in range(3): new_state[F_adj["L"][i]] = new_state[F_adj["D"][i]]
        for i in range(3): new_state[F_adj["D"][i]] = new_state[F_adj["R"][i]]
        for i in range(3): new_state[F_adj["R"][i]] = temp[F_adj["U"][i]]

    elif move == "F'":
        _rotate_face_counter_clockwise(new_state, "F")
        temp = {s: new_state[s] for s in F_adj["U"]}
        for i in range(3): new_state[F_adj["U"][i]] = new_state[F_adj["R"][i]]
        for i in range(3): new_state[F_adj["R"][i]] = new_state[F_adj["D"][i]]
        for i in range(3): new_state[F_adj["D"][i]] = new_state[F_adj["L"][i]]
        for i in range(3): new_state[F_adj["L"][i]] = temp[F_adj["U"][i]]

    elif move == "B":
        _rotate_face_clockwise(new_state, "B")
        temp = {s: new_state[s] for s in B_adj["U"]}
        for i in range(3): new_state[B_adj["U"][i]] = new_state[B_adj["R"][i]]
        for i in range(3): new_state[B_adj["R"][i]] = new_state[B_adj["D"][i]]
        for i in range(3): new_state[B_adj["D"][i]] = new_state[B_adj["L"][i]]
        for i in range(3): new_state[B_adj["L"][i]] = temp[B_adj["U"][i]]

    elif move == "B'":
        _rotate_face_counter_clockwise(new_state, "B")
        temp = {s: new_state[s] for s in B_adj["U"]}
        for i in range(3): new_state[B_adj["U"][i]] = new_state[B_adj["L"][i]]
        for i in range(3): new_state[B_adj["L"][i]] = new_state[B_adj["D"][i]]
        for i in range(3): new_state[B_adj["D"][i]] = new_state[B_adj["R"][i]]
        for i in range(3): new_state[B_adj["R"][i]] = temp[B_adj["U"][i]]


    elif move == "U2":
        new_state = apply_move_to_state(new_state, "U")
        new_state = apply_move_to_state(new_state, "U")
    elif move == "D2":
        new_state = apply_move_to_state(new_state, "D")
        new_state = apply_move_to_state(new_state, "D")
    elif move == "L2":
        new_state = apply_move_to_state(new_state, "L")
        new_state = apply_move_to_state(new_state, "L")
    elif move == "R2":
        new_state = apply_move_to_state(new_state, "R")
        new_state = apply_move_to_state(new_state, "R")
    elif move == "F2":
        new_state = apply_move_to_state(new_state, "F")
        new_state = apply_move_to_state(new_state, "F")
    elif move == "B2":
        new_state = apply_move_to_state(new_state, "B")
        new_state = apply_move_to_state(new_state, "B")

    return new_state



MOVES = {
    "U": ["U", "U'", "U2"],
    "D": ["D", "D'", "D2"],
    "L": ["L", "L'", "L2"],
    "R": ["R", "R'", "R2"],
    "F": ["F", "F'", "F2"],
    "B": ["B", "B'", "B2"]
}



ALL_MOVES = [
    "U", "U'", "U2",
    "D", "D'", "D2",
    "L", "L'", "L2",
    "R", "R'", "R2",
    "F", "F'", "F2",
    "B", "B'", "B2"
]
