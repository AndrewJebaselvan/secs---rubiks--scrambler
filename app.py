
from secs.utils import generate_scramble, apply_scramble
from secs.cube_state import CubeState
from secs.looped_phased_solver import looped_phased_solve

def main():


    scramble_input = input("Enter scramble moves separated by space (or press Enter for random scramble): ").strip()
    


    if scramble_input:
        scramble = scramble_input.split()
    else:
        scramble = generate_scramble(n=15) 
        

    print(f"\n=== Scramble: {' '.join(scramble)} ===")


    cube = CubeState()
    scrambled_state = apply_scramble(cube, scramble)



    print("\n--- Scrambled Cube State ---")
    for face in "UDFBLR":

        sticker_colors = [scrambled_state['cube'].get(f'{face}{i}', '?') for i in range(9)]
        print(f"{face}: {sticker_colors}")


    solution_moves = looped_phased_solve(scrambled_state)


    print("\n=== SOLUTION FOUND ===")
    print(f"Solved in {len(solution_moves)} moves:")
    print(' '.join(solution_moves))

if __name__ == "__main__":
    main()
