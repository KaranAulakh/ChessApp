class Piece:
    name = None
    isWhite = None

    def __init__(self, name, isWhite):
        self.name, self.isWhite = name, isWhite

    def isValidPieceAtLocation(self, x, y, piece_positions, typeName):
        if (0 <= x <= 7) and (0 <= y <= 7) \
           and piece_positions[str(x) + str(y)] is not None \
           and typeName in piece_positions[str(x) + str(y)].name:
            return True
        print("xy: " + str(x) + str(y) + " typename: " + typeName)
        return False

    def calculate_possible_moves():
        NotImplementedError("Subclass Must Implement this Method")
