from game.Piece import Piece

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
            if self.isValidPieceAtLocation(x + dx, y + dy, piece_positions, opponent, True):
                possible_moves.append(str(x + dx) + str(y + dy))

        return possible_moves
    

    def handle_castling(self, square, piece_positions):
        possible_castles = {}
        x, y = int(square[0]), int(square[1])
        if self.can_castle(x, 7, y, piece_positions):
            if self.isWhite:
                possible_castles["67"] = "shortWhite"
            else:
                possible_castles["60"] = "shortBlack"
        if self.can_castle(x, 0, y, piece_positions):
            if self.isWhite:
                possible_castles["27"] = "longWhite"
            else: 
                possible_castles["20"] = "longBlack"

        return possible_castles

    
    def can_castle(self, x_king, x_rook, y, piece_positions):
        if not self.isValidPieceAtLocation(x_rook, y, piece_positions, "Rook") \
           or not piece_positions[str(x_rook) + str(y)].is_first_move:
            return False
        
        # false if any squares in between are occupied
        for x in range (min(x_king, x_rook) + 1, max(x_king, x_rook)):
            # move king clooser to rook
            if str(x) + str(y) in piece_positions:
                return False
        return True



