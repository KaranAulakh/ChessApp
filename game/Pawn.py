from .Piece import Piece

class Pawn(Piece):
    promotion_row = None
    first_move = None
    move_increment = None

    def __init__(self, name, isWhite):
        super().__init__(name, isWhite)
        self.first_move = True
        self.promotion_row = 0 if isWhite else 7
        self.move_increment = -1 if isWhite else 1

    def calculatePossibleMoves(self, square):
        possible_moves = []
        y_coordinate = int(square[1]) + self.move_increment
        possible_moves.append(str(square[0]) + str(y_coordinate))

        if self.first_move:
            y_coordinate = int(square[1]) + self.move_increment + self.move_increment
            possible_moves.append(str(square[0]) + str(y_coordinate))

        return possible_moves
            


