from game.Piece import Piece

class King(Piece):
    # will be used to determine if king can castle
    is_first_move = True
    advance_increment = None

    def __init__(self, is_white):
        super().__init__("WhiteKing" if is_white else "BlackKing", is_white)
        self.advance_increment = -1 if is_white else 1

    def calculate_possible_moves(self, square, piece_positions):
        possible_moves = []
        x, y = int(square[0]), int(square[1])
        opponent = "Black" if self.is_white else "White"
        
        # check moves starting up, then spinning clockwise
        possible_squares = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for dx, dy in possible_squares:
            if self.is_valid_piece_at_location(x + dx, y + dy, piece_positions, opponent, True):
                possible_moves.append(str(x + dx) + str(y + dy))

        return possible_moves
    

    def handle_castling(self, square, piece_positions):
        possible_castles = {}
        if not self.is_first_move:
            return possible_castles
        
        x, y = int(square[0]), int(square[1])
        if self.can_castle(x, 7, y, piece_positions):
            if self.is_white:
                possible_castles["67"] = "shortWhite"
            else:
                possible_castles["60"] = "shortBlack"
        if self.can_castle(x, 0, y, piece_positions):
            if self.is_white:
                possible_castles["27"] = "longWhite"
            else: 
                possible_castles["20"] = "longBlack"

        return possible_castles

    
    def can_castle(self, x_king, x_rook, y, piece_positions):
        if not self.is_valid_piece_at_location(x_rook, y, piece_positions, "Rook") \
           or not piece_positions[str(x_rook) + str(y)].is_first_move:
            return False
        
        # false if any squares in between are occupied or under attack by opponent
        for x in range (min(x_king, x_rook) + 1, max(x_king, x_rook)):
            if str(x) + str(y) in piece_positions or self.is_in_check(str(x) + str(y), piece_positions):
                return False
        return True
    
    def is_in_check(self, square, piece_positions):
        x, y = int(square[0]), int(square[1])
        opponent = "Black" if self.is_white else "White"

        # Check if there's an opponent queen or bishop eyeing the queen 
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dx, dy in directions:
            x_increment, y_increment = x + dx, y + dy
            while 0 <= x_increment <= 7 and 0 <= y_increment <= 7:
                if str(x_increment) + str(y_increment) in piece_positions:
                    piece_name = piece_positions[str(x_increment) + str(y_increment)].name
                    if opponent in piece_name and ("Bishop" in piece_name or "Queen" in piece_name):
                        return True
                    break
                x_increment += dx
                y_increment += dy
        
        # check if there is an opponent rook or queen eyeing the queen
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            x_increment, y_increment = x + dx, y + dy
            while 0 <= x_increment <= 7 and 0 <= y_increment <= 7:
                if str(x_increment) + str(y_increment) in piece_positions:
                    piece_name = piece_positions[str(x_increment) + str(y_increment)].name
                    if opponent in piece_name and ("Rook" in piece_name or "Queen" in piece_name):
                        return True
                    break
                x_increment += dx
                y_increment += dy
        
        # check if there is an opponent knight eyeing the queen 
        possible_squares = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for dx, dy in possible_squares:
            if self.is_valid_piece_at_location(x + dx, y + dy, piece_positions, opponent + "Knight", False):
                return True
            
        # Check for captures
        for dx in [-1, 1]:
            if self.is_valid_piece_at_location(x + dx, y + self.advance_increment, piece_positions, opponent + "Pawn", False):
                return True

        return False



