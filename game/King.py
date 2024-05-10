from .Piece import Piece

class King(Piece):
    # will be used to determine if king can castle
    first_move = None

    def __init__(self, name, isWhite):
        super().__init__(name, isWhite)
        self.first_move = True

    def calculatePossibleMoves(self, square):
        possible_moves = []
        y_coordinate = int(square[1]) + self.move_increment
        possible_moves.append(str(square[0]) + str(y_coordinate))

        if self.first_move:
            y_coordinate = int(square[1]) + self.move_increment + self.move_increment
            possible_moves.append(str(square[0]) + str(y_coordinate))

        return possible_moves


