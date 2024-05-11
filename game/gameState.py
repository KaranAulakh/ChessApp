from .Util import Util

class GameState:
    piece_positions = {}

    def __init__(self):
        self.piece_positions = Util.get_start_piece_position()

    # Reset to the starting position
    def get_start_position(self):
        self.piece_positions = Util.get_start_piece_position()
        return self.get_serialized_piece_positions()
    
    def find_moves(self, square):
        return self.piece_positions[square].calculate_possible_moves(square, self.piece_positions)
    
    def move(self, start_square, destination_square):
        self.piece_positions[destination_square] = self.piece_positions.pop(start_square)
        return self.get_serialized_piece_positions()
    
    def get_serialized_piece_positions(self):
        seralized_positions = {}
        for position, piece in self.piece_positions.items():
            seralized_positions[position] = piece.name  
    
        return seralized_positions