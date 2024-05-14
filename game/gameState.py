from game.Pawn import Pawn
from game.Rook import Rook
from game.King import King
from game.Bishop import Bishop
from game.Queen import Queen
from game.Knight import Knight

class GameState:
    piece_positions = {}
    possible_castles = {}
    possible_moves = []
    en_passant_positions = None

    def __init__(self):
        self.piece_positions = self.get_start_piece_position()

    # Reset to the starting position
    def get_start_position(self):
        self.piece_positions = self.get_start_piece_position()
        return self.get_serialized_piece_positions()

    def find_moves(self, square):
        if "Pawn" in self.piece_positions[square].name:
            en_passant_position = self.en_passant_positions[1] if self.en_passant_positions is not None else None
            self.possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions, en_passant_position)
        else:
            self.possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions)
        return self.add_castling(square)
    
    def add_castling(self, square):
        # add any special moves to special moves dictionary
        if "King" in self.piece_positions[square].name:
            self.possible_castles = self.piece_positions[square].handle_castling(square, self.piece_positions)
        
        # add any special moves to possible moves list
        if self.possible_castles:
            for key in self.possible_castles.keys():
                self.possible_moves.append(key)

        return self.possible_moves

    def move(self, start_square, destination_square):
        # set en-passant location if pawn double stepped but save the location from the previous move
        previous_double_step = None
        if self.en_passant_positions is not None:
            previous_double_step = self.en_passant_positions
        self.en_passant_positions = self.get_en_passant_location(start_square, destination_square)

        # move piece to destination
        self.piece_positions[destination_square] = self.piece_positions.pop(start_square)
        
        # handling castling
        if (destination_square in self.possible_castles):
            self.castle(self.possible_castles[destination_square])

        # handling en passant pawn elimination
        if (previous_double_step is not None and destination_square == previous_double_step[1]):
            self.piece_positions.pop(previous_double_step[0])

        return self.get_serialized_piece_positions()
    
    
    def get_en_passant_location(self, start_square, destination_square):
        if "Pawn" in self.piece_positions[start_square].name and \
              self.piece_positions[start_square].is_double_step(start_square[1], destination_square[1]):
                skipped_square = str(start_square[0]) + str(max(int(destination_square[1]), int(start_square[1])) - 1)
                return [destination_square, skipped_square]
        return None


    def castle(self, castle_type):
        if castle_type == "shortWhite":
            self.piece_positions["57"] = self.piece_positions.pop("77")
        elif castle_type == "longWhite":
            self.piece_positions["37"] = self.piece_positions.pop("07")
        elif castle_type == "shortBlack":
            self.piece_positions["50"] = self.piece_positions.pop("70")
        elif castle_type == "longBlack":
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