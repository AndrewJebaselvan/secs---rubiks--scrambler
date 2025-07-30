from secs.cube_state import CubeState
from secs.utils import print_cube, apply_scramble, generate_scramble
from secs.moves import apply_move_to_state
from secs.looped_phased_solver import looped_phased_solve

def main():
    # Ask for user input
    raw_input = input("Enter scramble moves separated by space (or press Enter for random scramble): ").strip()
    
    # Parse scramble
    if raw_input:
        scramble = raw_input.split()
    else:
        scramble = generate_scramble(6)

    print(f"\n=== Scramble: {scramble} ===\n")

    # Create initial cube
    cube = CubeState()
    
    # Apply scramble
    apply_scramble(cube, scramble, apply_move_to_state)

    print("--- Scrambled Cube State ---")
    print_cube(cube.state)

    # Solve using looped SECS++
    print("\n=== PHASE: CROSS ===")
    result = looped_phased_solve({"cube": cube.state})

    # Print solved cube
    print("\n✅ Solved Cube State:")
    print_cube(cube.state)

    print(f"\nMoves to solve: {result}")

if __name__ == "__main__":
    main()
