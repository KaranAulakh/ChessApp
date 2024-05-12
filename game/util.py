from .Pawn import Pawn
from .Rook import Rook
from .King import King
from .Bishop import Bishop
from .Queen import Queen
from .Knight import Knight

class Util:

    @staticmethod
    def get_start_piece_position():
        positions = {
            # White Back Row
            "07": Rook(True),
            "17": Knight(True),
            "27": Bishop(True),
            "37": Queen(True),
            "47": King(True),
            "57": Bishop(True),
            "67": Knight(True),
            "77": Rook(True),
            # Black Back Row
            "00": Rook(False),
            "10": Knight(False),
            "20": Bishop(False),
            "30": Queen(False),
            "40": King(False),
            "50": Bishop(False),
            "60": Knight(False),
            "70": Rook(False),
        }

        # add white pawns
        for i in range(8):
            positions[str(i) + "6"] = Pawn(True)

        # add black pawns
        for i in range(8):
            positions[str(i) + "1"] = Pawn(False)
        
        return positions
