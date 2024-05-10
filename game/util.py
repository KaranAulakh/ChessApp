from game.Pawn import Pawn

class Util:

    @staticmethod
    def get_start_piece_positions():
        positions = {
            "07": Pawn("Pawn", True, "LightKing"),
            "17": Pawn("Pawn", True, "LightKing"),
            "27": Pawn("Pawn", True, "LightKing"),
            "37": Pawn("Pawn", True, "LightKing"),
            "47": Pawn("Pawn", True, "LightKing"),
            "57": Pawn("Pawn", True, "LightKing"),
            "67": Pawn("Pawn", True, "LightKing"),
            "77": Pawn("Pawn", True, "LightKing"),
            "00": Pawn("Pawn", True, "LightKing"),
            "10": Pawn("Pawn", True, "LightKing"),
            "20": Pawn("Pawn", True, "LightKing"),
            "30": Pawn("Pawn", True, "LightKing"),
            "40": Pawn("Pawn", True, "LightKing"),
            "50": Pawn("Pawn", True, "LightKing"),
            "60": Pawn("Pawn", True, "LightKing"),
            "70": Pawn("Pawn", True, "LightKing"),
        }
        # add light pawns
        for i in range(8):
            positions[str(i) + "6"] = Pawn("Pawn", True, "LightPawn")

        # add dark pawns
        for i in range(8):
            positions[str(i) + "1"] = Pawn("Pawn", False, "DarkPawn")
        
        return positions
