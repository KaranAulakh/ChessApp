from .Util import Util

class GameState:
    piece_positions = {}

    def __init__(self):
        self.piece_positions = Util.get_start_piece_positions()

    def get_seralized_piece_positions(self):
        serialized_positions = {}
        for position, piece in self.piece_positions.items():
            serialized_positions[position] = piece.name  
    
        return serialized_positions
    
    def find_moves(self, square):
        return self.piece_positions[square].calculatePossibleMoves(square)