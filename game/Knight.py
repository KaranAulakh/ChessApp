from game.Piece import Piece

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
            if self.isValidPieceAtLocation(x + dx, y + dy, piece_positions, opponent, True):
                possible_moves.append(str(x + dx) + str(y + dy))

        return possible_moves



