from game.Util import Util

class GameState:
    piece_positions = {}

    def __init__(self):
        self.piece_positions = Util.get_start_piece_positions()

    def get_piece_at(self, x, y):
        return self.piece_positions["{x}{y}"]
    
    def move(self, move):
        return move
