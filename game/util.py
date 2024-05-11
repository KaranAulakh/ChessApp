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
            "00": Rook("BlackRook", False),
            "10": King("BlackKing", False),
            "20": King("BlackKing", False),
            "30": King("BlackKing", False),
            "40": King("BlackKing", False),
            "50": King("BlackKing", False),
            "60": King("BlackKing", False),
            "70": Rook("BlackRook", False),
        }

        # add white pawns
        for i in range(8):
            positions[str(i) + "6"] = Pawn("WhitePawn", True)

        # add black pawns
        for i in range(8):
            positions[str(i) + "1"] = Pawn("BlackPawn", False)
        
        return positions
