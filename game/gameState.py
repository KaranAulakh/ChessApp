from game.Pawn import Pawn
from game.Rook import Rook
from game.King import King
from game.Bishop import Bishop
from game.Queen import Queen
from game.Knight import Knight

class GameState:
    piece_positions = {}
    special_moves = {}
    possible_moves = []

    def __init__(self):
        self.piece_positions = self.get_start_piece_position()

    # Reset to the starting position
    def get_start_position(self):
        self.piece_positions = self.get_start_piece_position()
        return self.get_serialized_piece_positions()

    def find_moves(self, square):
        self.possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions)
        return self.add_special_moves(square)
    
    def add_special_moves(self, square):
        # add any special moves to special moves dictionary
        if "King" in self.piece_positions[square].name or "Pawn" in self.piece_positions[square].name:
            self.special_moves = self.piece_positions[square].handle_special_moves(square, self.piece_positions)
        
        # add any special moves to possible moves list
        if self.special_moves:
            for key in self.special_moves.keys():
                self.possible_moves.append(key)

        return self.possible_moves

    def move(self, start_square, destination_square):
        if (destination_square in self.special_moves):
            self.execute_special_move(destination_square)
        self.piece_positions[destination_square] = self.piece_positions.pop(start_square)
        return self.get_serialized_piece_positions()
    

    def execute_special_move(self, destination_square):
        if self.special_moves[destination_square] == "shortWhite":
            self.piece_positions["57"] = self.piece_positions.pop("77")
        elif self.special_moves[destination_square] == "longWhite":
            self.piece_positions["37"] = self.piece_positions.pop("07")
        elif self.special_moves[destination_square] == "shortBlack":
            self.piece_positions["50"] = self.piece_positions.pop("70")
        elif self.special_moves[destination_square] == "longBlack":
            self.piece_positions["30"] = self.piece_positions.pop("00")

    def get_serialized_piece_positions(self):
        serialized_positions = {}
        for position, piece in self.piece_positions.items():
            serialized_positions[position] = piece.name

        return serialized_positions
    
    def get_start_piece_position(self):
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