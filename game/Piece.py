class Piece:
    name = None
    isWhite = None

    def __init__(self, name, isWhite):
        self.name, self.isWhite = name, isWhite

    def isValidPieceAtLocation(self, x, y, piece_positions, typeName, canBeEmpty = False):
        if (0 <= x <= 7) and (0 <= y <= 7):
            if canBeEmpty and str(x) + str(y) not in piece_positions:
                return True
            if str(x) + str(y) in piece_positions and typeName in piece_positions[str(x) + str(y)].name:
                return True
        return False
    
    def calculate_possible_moves():
        NotImplementedError("Subclass Must Implement this Method")
