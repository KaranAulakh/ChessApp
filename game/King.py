from .Piece import Piece

class King(Piece):
    # will be used to determine if king can castle
    is_first_move = True

    def __init__(self, isWhite):
        super().__init__("WhiteKing" if isWhite else "BlackKing", isWhite)

    def calculate_possible_moves(self, square, piece_positions):
        possible_moves = []
        x, y = int(square[0]), int(square[1])
        opponent = "Black" if self.isWhite else "White"
        
        # check moves starting up, then spinning clockwise
        possible_squares = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for dx, dy in possible_squares:
            if (str(x + dx) + str(y + dy) not in piece_positions) or (str(x + dx) + str(y + dy) in piece_positions and opponent in piece_positions[str(x + dx) + str(y + dy)].name) and (0 <= x + dx <= 7) and (0 <= y + dy <= 7):
                possible_moves.append(str(x + dx) + str(y + dy))

        return possible_moves


