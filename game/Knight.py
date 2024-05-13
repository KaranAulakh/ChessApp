from .Piece import Piece

class Knight(Piece):
    def __init__(self, isWhite):
        super().__init__("WhiteKnight" if isWhite else "BlackKnight", isWhite)

    def calculate_possible_moves(self, square, piece_positions):
        possible_moves = []
        x, y = int(square[0]), int(square[1])
        opponent = "Black" if self.isWhite else "White"

        # Add all squares that are empty or occupied by the opponent
        possible_squares = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for dx, dy in possible_squares:
            if ((str(x + dx) + str(y + dy) not in piece_positions) or (str(x + dx) + str(y + dy) in piece_positions and opponent in piece_positions[str(x + dx) + str(y + dy)].name)) and (0 <= x + dx <= 7) and (0 <= y + dy <= 7):
                possible_moves.append(str(x + dx) + str(y + dy))

        return possible_moves



