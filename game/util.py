from .Pawn import Pawn
from .King import King

class Util:

    @staticmethod
    def get_start_piece_positions():
        '''
        positions = {
            "07": Pawn("LightKing", True),
            "17": Pawn("LightKing", True),
            "27": Pawn("LightKing", True),
            "37": Pawn("LightKing", True),
            "47": Pawn("LightKing", True),
            "57": Pawn("LightKing", True),
            "67": Pawn("LightKing", True),
            "77": Pawn("LightKing", True),
            "00": Pawn("LightKing", True),
            "10": Pawn("LightKing", True),
            "20": Pawn("LightKing", True),
            "30": Pawn("LightKing", True),
            "40": Pawn("LightKing", True),
            "50": Pawn("LightKing", True),
            "60": Pawn("LightKing", True),
            "70": Pawn("LightKing", True),
        }
        '''
        #for testing
        positions = {}
        for i in range(8):
            positions[str(i) + "7"] = King("LightKing", True)

        for i in range(8):
            positions[str(i) + "0"] = King("DarkKing", False)


        # add light pawns
        for i in range(8):
            positions[str(i) + "6"] = Pawn("LightPawn", True)

        # add dark pawns
        for i in range(8):
            positions[str(i) + "1"] = Pawn("DarkPawn", False)
        
        return positions
