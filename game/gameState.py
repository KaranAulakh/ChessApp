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
    black_king_position = "40"
    white_king_position = "47"
    en_passant_positions = None

    def __init__(self):
        self.piece_positions = self.get_start_piece_position()

    # Reset to the starting position
    def get_start_position(self):
        self.piece_positions = self.get_start_piece_position()
        return self.get_serialized_piece_positions()

    def find_moves(self, square):
        find_possible_moves = []
        if "Pawn" in self.piece_positions[square].name:
            en_passant_position = self.en_passant_positions[1] if self.en_passant_positions is not None else None
            find_possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions, en_passant_position)
        else:
            find_possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions)

        # delete moves that place king in check
        legal_moves = []
        king_position = self.white_king_position if self.piece_positions[square].isWhite else self.black_king_position
        for end_square in find_possible_moves:
            # Update the king_position if the king is moving
            if "King" in self.piece_positions[square].name:
                king_position = end_square
            
            # perform the move to get the temp position and check if king is in check
            test_position = self.perform_move(square, end_square, True)
            if not test_position[king_position].is_in_check(king_position, test_position):
                legal_moves.append(end_square)
        
        # set the possible moves and add castling
        self.possible_moves = legal_moves 
        return self.add_castling(square)
    
    def add_castling(self, square):
        # add any special moves to special moves dictionary
        if not "King" in self.piece_positions[square].name:
            return self.possible_moves
        
        # add any special moves to possible moves list
        self.possible_castles = self.piece_positions[square].handle_castling(square, self.piece_positions)
        if self.possible_castles:
            for key in self.possible_castles.keys():
                self.possible_moves.append(key)

        return self.possible_moves

    def move(self, start_square, destination_square):
        self.piece_positions = self.perform_move(start_square, destination_square, False)
        return self.get_serialized_piece_positions()

    
    def perform_move(self, start_square, destination_square, test_move = True):
        piece_positions = self.piece_positions.copy()
        # set en-passant location if pawn double stepped but save the location from the previous move
        previous_double_step = None
        if self.en_passant_positions is not None:
            previous_double_step = self.en_passant_positions

        # don't reset en_passant value if this is just a test move
        if not test_move:
            self.en_passant_positions = self.get_en_passant_location(start_square, destination_square)

        # move piece to destination
        piece_positions[destination_square] = piece_positions.pop(start_square)
        
        # handle castling
        if (destination_square in self.possible_castles):
            piece_positions = self.castle(self.possible_castles[destination_square], piece_positions)

        # handling en passant pawn elimination
        if (previous_double_step is not None and destination_square == previous_double_step[1]):
            piece_positions.pop(previous_double_step[0])

        # keep track of King
        if not test_move:
            if start_square == self.black_king_position:
                self.black_king_position = destination_square
            elif start_square == self.white_king_position:
                self.white_king_position = destination_square

        return piece_positions

    def get_en_passant_location(self, start_square, destination_square):
        if "Pawn" in self.piece_positions[start_square].name and \
              self.piece_positions[start_square].is_double_step(start_square[1], destination_square[1]):
                skipped_square = str(start_square[0]) + str(max(int(destination_square[1]), int(start_square[1])) - 1)
                return [destination_square, skipped_square]
        return None


    def castle(self, castle_type, piece_positions):
        if castle_type == "shortWhite":
            piece_positions["57"] = piece_positions.pop("77")
        elif castle_type == "longWhite":
            piece_positions["37"] = piece_positions.pop("07")
        elif castle_type == "shortBlack":
            piece_positions["50"] = piece_positions.pop("70")
        elif castle_type == "longBlack":
            piece_positions["30"] = piece_positions.pop("00")

        return piece_positions

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