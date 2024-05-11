class Piece:
    name = None
    isWhite = None

    def __init__(self, name, isWhite):
        self.name, self.isWhite = name, isWhite

    def calculate_possible_moves():
        NotImplementedError("Subclass Must Implement this Method")
