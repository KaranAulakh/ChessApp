from game.Piece import Piece

class Pawn(Piece):
    promotion_row = None
    first_move = None

    def __init__(self, name, isWhite, imageName):
        super().__init__(name, isWhite, imageName)
        self.first_move = True
        self.promotion_row = 0 if isWhite else 7

    def move():
        pass


