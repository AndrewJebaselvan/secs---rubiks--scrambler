class CubeState:
    def __init__(self, flat_dict=None):
        if flat_dict:
            self.state = dict(flat_dict)
        else:
            self.state = self.get_solved_state()

    def get_solved_state(self):
        return {
            f"{face}{i}": face
            for face in "UDFBLR"
            for i in range(9)
        }
