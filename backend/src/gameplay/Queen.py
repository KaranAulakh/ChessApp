from gameplay.Piece import Piece

class Queen(Piece):
    def __init__(self, is_white):
        super().__init__("WhiteQueen" if is_white else "BlackQueen", is_white)

    def calculate_possible_moves(self, square, piece_positions):
        possible_moves = []
        x, y = int(square[0]), int(square[1])
        opponent = "Black" if self.is_white else "White"
        
        # check moves starting up, then spinning clockwise
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
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