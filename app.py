import kociemba
from secs.utils import generate_scramble, cubestring_to_dict
from secs.looped_phased_solver import looped_phased_solve
from secs.moves import apply_move_to_state
from secs.cube_state import CubeState

def main():
    """Main function to run the SECS++ solver."""
    scramble_input = input("Enter scramble moves separated by space (or press Enter for random scramble): ").strip()
    
    scramble_moves = scramble_input.split() if scramble_input else generate_scramble(15)

    print(f"\n=== Scramble: {scramble_moves} ===")

    # Create a guaranteed-valid cubestring for Kociemba
    # Start with a solved cube
    cube = CubeState()
    temp_state = cube.get_solved_state()
    # Apply our own move logic to scramble it
    for move in scramble_moves:
        temp_state = apply_move_to_state(temp_state, move)
    
    # Convert our dictionary state to the Kociemba string format
    face_order_map = "URFDLB"
    initial_cubestring = ""
    for face in face_order_map:
        for i in range(9):
            initial_cubestring += temp_state.get(f'{face}{i}', '?')

    # Convert the dictionary state for our solver
    scrambled_state = {"cube": temp_state}

    print("\n--- Scrambled Cube State ---")
    for face in "UDFBLR":
        print(f"{face}: {[scrambled_state['cube'][f'{face}{i}'] for i in range(9)]}")

    # Pass both the dictionary state and the valid string to the solver
    solution_moves = looped_phased_solve(scrambled_state, initial_cubestring)

    print("\n=== SOLUTION FOUND ===")
    if isinstance(solution_moves, list):
        print(f"Solved with SECS++ in {len(solution_moves)} moves:")
        print(' '.join(solution_moves))
    else: # Kociemba returns a string
        print(f"Solved with Kociemba Fallback in {len(solution_moves.split())} moves:")
        print(solution_moves)

if __name__ == "__main__":
    main()

