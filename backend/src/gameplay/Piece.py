class Piece:
    name = None
    is_white = None

    def __init__(self, name, is_white):
        self.name, self.is_white = name, is_white

    def is_valid_piece_at_location(self, x, y, piece_positions, typeName, canBeEmpty = False):
        if (0 <= x <= 7) and (0 <= y <= 7):
            if canBeEmpty and str(x) + str(y) not in piece_positions:
                return True
            if str(x) + str(y) in piece_positions and typeName in piece_positions[str(x) + str(y)].name:
                return True
        return False
    
    def calculate_possible_moves():
        NotImplementedError("Subclass Must Implement this Method")