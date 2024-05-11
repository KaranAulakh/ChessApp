from .Piece import Piece

class King(Piece):
    # will be used to determine if king can castle
    is_first_move = True

    def __init__(self, name, isWhite):
        super().__init__(name, isWhite)

    def calculate_possible_moves(self, square):
        possibleMoves = ["44"]

        return possibleMoves


