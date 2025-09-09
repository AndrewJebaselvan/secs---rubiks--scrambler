from flask import Flask, render_template, request, jsonify
import kociemba


from secs.looped_phased_solver import looped_phased_solve
from secs.cube_state import CubeState
from secs.moves import apply_move_to_state
from secs.utils import generate_scramble, dict_to_cubestring

app = Flask(__name__)

@app.route('/')
def home():
    """Serves the main web page."""
    return render_template('index.html')

@app.route('/api/scramble', methods=['GET'])
def get_scramble():
    """
    API endpoint to generate and return a random scramble.
    """
    scramble_moves = generate_scramble(15)
    return jsonify({'scramble': scramble_moves})


@app.route('/solve', methods=['POST'])
def solve_cube():
    """
    API endpoint to receive a scramble and return a solution.
    """
    try:
        data = request.get_json()
        scramble_moves = data.get('scrambleMoves', [])

        if not scramble_moves:
            return jsonify({'error': 'No scramble moves provided.'}), 400
        
        cube = CubeState()
        temp_state = cube.get_solved_state()
        
        
        for move in scramble_moves:
            temp_state = apply_move_to_state(temp_state, move)
        
        scrambled_state = {"cube": temp_state}
        initial_cubestring = dict_to_cubestring(temp_state)

        
        solution_moves = looped_phased_solve(scrambled_state, initial_cubestring)
        
        
        if isinstance(solution_moves, str):
            solution_moves = solution_moves.split()

        return jsonify({'solution': solution_moves})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    
    app.run(debug=True)
