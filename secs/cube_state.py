from secs.moves import apply_move_to_state

class CubeState:
    def __init__(self):
        self.state = self._create_solved()

    def _create_solved(self):
        faces = ["U", "D", "F", "B", "L", "R"]
        return {f"{face}{i}": face for face in faces for i in range(9)}

    def apply_move(self, move):
        self.state = apply_move_to_state({"cube": self.state}, move)
