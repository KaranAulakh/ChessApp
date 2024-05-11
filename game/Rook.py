from .Piece import Piece

class Rook(Piece):
    is_first_move = True

    def __init__(self, name, isWhite):
        super().__init__(name, isWhite)

    def calculate_possible_moves(self, square, piece_positions):
        possible_moves = []
        x, y = int(square[0]), int(square[1])
        opponent = "Black" if self.isWhite else "White"
        
        # check moves to the right, left, up, down respectively 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            x_increment, y_increment = x + dx, y + dy
            while 0 <= x_increment <= 7 and 0 <= y_increment <= 7:
                if str(x_increment) + str(y_increment) in piece_positions:
                    if opponent in piece_positions[str(x_increment) + str(y_increment)].name:
                        possible_moves.append(str(x_increment) + str(y_increment))
                    break
                else:
                    possible_moves.append(str(x_increment) + str(y_increment))
                x_increment += dx
                y_increment += dy

        return possible_moves