from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import kociemba

from secs.looped_phased_solver import looped_phased_solve
from secs.utils import dict_to_cubestring
from secs.cube_state import CubeState
from secs.moves import apply_move_to_state

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app) 

@app.route('/')
def serve_index():
    """Serves the main index.html file to the browser."""
    return send_from_directory('.', 'index.html')

@app.route('/solve', methods=['POST'])
def solve_cube():
    """API endpoint to solve the cube."""
    try:
        data = request.get_json()
        if not data or 'scramble' not in data:
            return jsonify({'error': 'No scramble string provided.'}), 400

        scramble_moves = data['scramble'].split()
        print(f"Received scramble: {' '.join(scramble_moves)}")

        # --- Create a valid cube state using our corrected move engine ---
        current_cube_dict = CubeState().get_solved_state()
        for move in scramble_moves:
            current_cube_dict = apply_move_to_state(current_cube_dict, move)
        
        scrambled_state = {"cube": current_cube_dict}
        # Create the cubestring needed for the Kociemba failover
        initial_cubestring = dict_to_cubestring(current_cube_dict)
        
        # --- Run our hybrid solver ---
        solution_moves, solver_type = looped_phased_solve(scrambled_state, initial_cubestring)

        return jsonify({
            'solver_type': solver_type,
            'solution_moves': solution_moves,
            'move_count': len(solution_moves)
        })

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    print("Starting SECS++ Flask Server...")
    print("Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, host='127.0.0.1', port=5000)

