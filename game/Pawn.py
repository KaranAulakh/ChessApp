from .Piece import Piece

class Pawn(Piece):
    promotion_row = None
    start_row = None
    move_increment = None

    def __init__(self, name, isWhite):
        super().__init__(name, isWhite)
        self.start_row = 6 if isWhite else 1
        self.promotion_row = 0 if isWhite else 7
        self.move_increment = -1 if isWhite else 1

    def calculatePossibleMoves(self, square, piece_positions):
        possible_moves = []
        x = int(square[0])
        y = int(square[1]) + self.move_increment
        opponent = "Black" if self.isWhite else "White"


        # Add possible captures
        print(str(x+1) + str(y) in piece_positions and opponent in (piece_positions[str(x+1) + str(y)].name))
        if (str(x+1) + str(y) in piece_positions and opponent in (piece_positions[str(x+1) + str(y)].name)):
            possible_moves.append(str(x+1) + str(y))
        
        print(str(x-1) + str(y) in piece_positions and opponent in piece_positions[str(x-1) + str(y)].name)
        if (str(x-1) + str(y) in piece_positions and opponent in piece_positions[str(x-1) + str(y)].name):
            possible_moves.append(str(x-1) + str(y))
        
        # Add single space advance or return if blocked
        if (str(x) + str(y) in piece_positions or y < 0 or y > 7):
            return possible_moves
        possible_moves.append(str(x) + str(y))

        # Add double space advance if available
        if (self.start_row == int(square[1])):
            y += self.move_increment
            if (str(x) + str(y) in piece_positions or y < 0 or y > 7):
                return possible_moves
            possible_moves.append(str(square[0]) + str(y))

        return possible_moves



