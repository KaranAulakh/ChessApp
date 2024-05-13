from game.Piece import Piece

class Pawn(Piece):
    promotion_row = None
    start_row = None
    move_increment = None

    def __init__(self, isWhite):
        super().__init__("WhitePawn" if isWhite else "BlackPawn", isWhite)
        self.start_row = 6 if isWhite else 1
        self.promotion_row = 0 if isWhite else 7
        self.move_increment = -1 if isWhite else 1

    def calculate_possible_moves(self, square, piece_positions):
        possible_moves = []
        x, y = int(square[0]), int(square[1]) + self.move_increment
        opponent = "Black" if self.isWhite else "White"


        # Check for captures
        for dx in [-1, 1]:
            if self.isValidPieceAtLocation(x + dx, y, piece_positions, opponent, False):
                possible_moves.append(str(x + dx) + str(y))
        
        # Add single space advance or return if blocked
        if (str(x) + str(y) not in piece_positions and 0 <= y <= 7):
            possible_moves.append(str(x) + str(y))
            # Add double space advance if available
            y += self.move_increment
            if (self.start_row == int(square[1]) and str(x) + str(y) not in piece_positions and 0 <= y <= 7):
                possible_moves.append(str(square[0]) + str(y))

        return possible_moves
    
    def handle_special_moves(self, square, piece_positions):
        return {}



