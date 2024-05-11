from .Pawn import Pawn
from .King import King

class Util:

    @staticmethod
    def get_start_piece_positions():
        '''
        positions = {
            "07": Pawn("WhiteKing", True),
            "17": Pawn("WhiteKing", True),
            "27": Pawn("WhiteKing", True),
            "37": Pawn("WhiteKing", True),
            "47": Pawn("WhiteKing", True),
            "57": Pawn("WhiteKing", True),
            "67": Pawn("WhiteKing", True),
            "77": Pawn("WhiteKing", True),
            "00": Pawn("WhiteKing", True),
            "10": Pawn("WhiteKing", True),
            "20": Pawn("WhiteKing", True),
            "30": Pawn("WhiteKing", True),
            "40": Pawn("WhiteKing", True),
            "50": Pawn("WhiteKing", True),
            "60": Pawn("WhiteKing", True),
            "70": Pawn("WhiteKing", True),
        }
        '''
        #for testing
        positions = {}
        for i in range(8):
            positions[str(i) + "7"] = King("WhiteKing", True)

        for i in range(8):
            positions[str(i) + "0"] = King("BlackKing", False)


        # add white pawns
        for i in range(8):
            positions[str(i) + "6"] = Pawn("WhitePawn", True)

        # add black pawns
        for i in range(8):
            positions[str(i) + "1"] = Pawn("BlackPawn", False)
        
        return positions
