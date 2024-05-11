from .Util import Util

class GameState:
    piece_positions = {}

    def __init__(self):
        self.piece_positions = Util.get_start_piece_positions()

    # Reset to the starting position
    def get_start_position(self):
        self.piece_positions = Util.get_start_piece_positions()
        return self.get_seralized_piece_positions()
    
    def find_moves(self, square):
        return self.piece_positions[square].calculatePossibleMoves(square)
    
    def move(self, start_square, destination_square):
        self.piece_positions[destination_square] = self.piece_positions.pop(start_square)
        return self.get_seralized_piece_positions()
    
    def get_seralized_piece_positions(self):
        serialized_positions = {}
        for position, piece in self.piece_positions.items():
            serialized_positions[position] = piece.name  
    
        return serialized_positions