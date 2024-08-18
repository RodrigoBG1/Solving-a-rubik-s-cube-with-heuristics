class Cube:
    def __init__(self):
        self.cube = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
        self.path = []
        self.move = ''
        self.distance = 0
        self.heuristic_value = 0
        self.cube_int_tuple = ()

    def __lt__(self, other):
        if not isinstance(other, Cube):
            return False
        
        return self.distance + self.heuristic_value < other.distance + other.heuristic_value

    def calculate_heuristic(self, heuristic):
        self.heuristic_value = heuristic(self)