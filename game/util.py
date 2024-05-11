from .Pawn import Pawn
from .Rook import Rook
from .King import King

class Util:

    @staticmethod
    def get_start_piece_position():
        positions = {
            "07": Rook("WhiteRook", True),
            "17": King("WhiteKing", True),
            "27": King("WhiteKing", True),
            "37": King("WhiteKing", True),
            "47": King("WhiteKing", True),
            "57": King("WhiteKing", True),
            "67": King("WhiteKing", True),
            "77": Rook("WhiteRook", True),
            "00": Rook("BlackRook", True),
            "10": King("BlackKing", True),
            "20": King("BlackKing", True),
            "30": King("BlackKing", True),
            "40": King("BlackKing", True),
            "50": King("BlackKing", True),
            "60": King("BlackKing", True),
            "70": Rook("BlackRook", True),
        }

        # add white pawns
        for i in range(8):
            positions[str(i) + "6"] = Pawn("WhitePawn", True)

        # add black pawns
        for i in range(8):
            positions[str(i) + "1"] = Pawn("BlackPawn", False)
        
        return positions
