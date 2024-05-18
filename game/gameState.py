from game.Pawn import Pawn
from game.Rook import Rook
from game.King import King
from game.Bishop import Bishop
from game.Queen import Queen
from game.Knight import Knight

class GameState:
    INITIAL_BLACK_KING_POSITION = "40"
    INITIAL_WHITE_KING_POSITION = "47"

    def __init__(self):
        self.piece_positions = self.get_start_piece_position()
        self.possible_castles = {}
        self.possible_moves = []
        self.black_king_position = self.INITIAL_BLACK_KING_POSITION
        self.white_king_position = self.INITIAL_WHITE_KING_POSITION
        self.en_passant_positions = None

    ''' METHODS TO FIND MOVES '''

    ''' Find all legal moves given the location of a piece '''
    def get_legal_moves(self, square):
        all_possible_moves = []
        if isinstance(self.piece_positions[square], Pawn):
            en_passant_position = self.en_passant_positions[1] if self.en_passant_positions is not None else None
            all_possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions, en_passant_position)
        else:
            all_possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions)

        self.possible_moves = self.delete_invalid_moves(square, all_possible_moves)
        return self.add_castling(square)
    
    ''' Delete any illegal moves (moves that place own King in check) '''
    def delete_invalid_moves(self, square, possible_moves):
        legal_moves = []
        king_position = self.white_king_position if self.piece_positions[square].is_white else self.black_king_position

        for end_square in possible_moves:
            # Update the king_position if the king itself is moving
            if isinstance(self.piece_positions[square], King):
                king_position = end_square
            
            # Perform the move to get the temp position and check if king is in check
            test_position = self.perform_move(square, end_square, True)
            if not test_position[king_position].is_in_check(king_position, test_position):
                legal_moves.append(end_square)
        
        return legal_moves 

    ''' Add castling moves if the piece to move is the King'''
    def add_castling(self, square):
        # add any special moves to special moves dictionary
        if not isinstance(self.piece_positions[square], King):
            return self.possible_moves
        
        # add any special moves to possible moves list
        self.possible_castles = self.piece_positions[square].handle_castling(square, self.piece_positions)
        if self.possible_castles:
            for key in self.possible_castles.keys():
                self.possible_moves.append(key)

        return self.possible_moves

    '''  Find the location of en_passant for the next move, if any '''
    def get_en_passant_location(self, start_square, destination_square):
        if isinstance(self.piece_positions[start_square], Pawn) and \
                      self.piece_positions[start_square].is_double_step(start_square[1], destination_square[1]):
            skipped_square = str(start_square[0]) + str(max(int(destination_square[1]), int(start_square[1])) - 1)
            return [destination_square, skipped_square]
        return None


    ''' METHODS TO HANDLE PIECE MOVEMENT '''

    ''' method to move piece in the game '''
    def move(self, start_square, destination_square):
        self.piece_positions = self.perform_move(start_square, destination_square, False)
        pawn_can_promote = None
        if isinstance(self.piece_positions[destination_square], Pawn) and \
            self.piece_positions[destination_square].can_promote(destination_square):
            pawn_can_promote = destination_square
        return { 
            "piecePositions":  self.get_serialized_piece_positions(),
            "pawnCanPromote": pawn_can_promote
        }
    
    ''' method to temporarily perform a move and return the position of all pieces after movement
        if test_move is True there will be no changes to stored variables in the GameState class '''
    def perform_move(self, start_square, destination_square, test_move = True):
        piece_positions = self.piece_positions.copy()

        # set en-passant location if pawn double stepped but save the location from the previous move
        previous_double_step = None
        if self.en_passant_positions is not None:
            previous_double_step = self.en_passant_positions

        # move piece to destination
        piece_positions[destination_square] = piece_positions.pop(start_square)
        
        # handle castling
        if (destination_square in self.possible_castles):
            piece_positions = self.castle(self.possible_castles[destination_square], piece_positions)

        # handling en passant pawn elimination
        if (previous_double_step is not None and destination_square == previous_double_step[1]):
            piece_positions.pop(previous_double_step[0])
        
        # update information only if it's a real move
        if not test_move:
            self.update_piece_metadata(piece_positions, start_square, destination_square)

        return piece_positions
    
    ''' Update en_passant_positions, first_move flags, and king_positions '''
    def update_piece_metadata(self, piece_positions, start_square, destination_square):
        self.en_passant_positions = self.get_en_passant_location(start_square, destination_square)

        # change first move bool if needed
        if isinstance(piece_positions[destination_square], King) or isinstance(piece_positions[destination_square], Rook):
            piece_positions[destination_square].is_first_move = False
        
        # keep track of King
        if start_square == self.black_king_position:
            self.black_king_position = destination_square
        elif start_square == self.white_king_position:
            self.white_king_position = destination_square
        
    
    ''' Move the Rook to the corresponding square to complete the castle '''
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
    
    def promote_pawn(self, pawn_location, promote_to):
        is_white = self.piece_positions[pawn_location].is_white
        if promote_to == "Queen":
            self.piece_positions[pawn_location] = Queen(is_white)
        elif promote_to == "Rook":
            self.piece_positions[pawn_location] = Rook(is_white)
        elif promote_to == "Bishop":
            self.piece_positions[pawn_location] = Bishop(is_white)
        elif promote_to == "Knight":
            self.piece_positions[pawn_location] = Knight(is_white)

        print(self.get_serialized_piece_positions)
        
        return self.get_serialized_piece_positions

    ''' UTILITY METHODS '''

    ''' Construct an Object for the front end. This is just an object of keys that represent location
        and piece names that consist of Black or White and the piece name '''
    def get_serialized_piece_positions(self):
        serialized_positions = {}
        for position, piece in self.piece_positions.items():
            serialized_positions[position] = piece.name

        return serialized_positions
        
    
    ''' Set/Reset the board to the starting position '''
    def get_start_position(self):
        self.piece_positions = self.get_start_piece_position()
        return self.get_serialized_piece_positions()
    
    ''' Define the intial piece positions on the board '''
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
    