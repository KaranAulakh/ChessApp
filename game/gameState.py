class GameState:
    def __init__(self):
        self.piece_positions = None

    def generate_piece_positions(self, move):
        if move == "Start":
            return self.start_position()
        else:
            # do something
            pass
        
    def start_position(self):
        return {
            "07": "LightRook",
            "17": "LightKnight",
            "27": "LightBishop",
            "37": "LightQueen",
            "47": "LightKing",
            "57": "LightBishop",
            "67": "LightKnight",
            "77": "LightRook",
            "00": "DarkRook",
            "10": "DarkKnight",
            "20": "DarkBishop",
            "30": "DarkQueen",
            "40": "DarkKing",
            "50": "DarkBishop",
            "60": "DarkKnight",
            "70": "DarkRook",
            "06": "LightPawn",
            "16": "LightPawn",
            "26": "LightPawn",
            "36": "LightPawn",
            "46": "LightPawn",
            "56": "LightPawn",
            "66": "LightPawn",
            "76": "LightPawn",
            "01": "DarkPawn",
            "11": "DarkPawn",
            "21": "DarkPawn",
            "31": "DarkPawn",
            "41": "DarkPawn",
            "51": "DarkPawn",
            "61": "DarkPawn",
            "71": "DarkPawn",
        }

    def get_piece_at(self, x, y):
        return self.piece_positions.get(f"{x}{y}")
