from .Piece import Piece

class Rook(Piece):
    is_first_move = True

    def __init__(self, name, isWhite):
        super().__init__(name, isWhite)

    def calculate_possible_moves(self, square, piece_positions):
        possibleMoves = ["44"]

        return possibleMoves