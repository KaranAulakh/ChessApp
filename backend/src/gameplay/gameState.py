from typing import Dict, List, Optional, Tuple, Union, Any
from gameplay.Pawn import Pawn
from gameplay.Rook import Rook
from gameplay.King import King
from gameplay.Bishop import Bishop
from gameplay.Queen import Queen
from gameplay.Knight import Knight
from gameplay.Piece import Piece

class GameState:
    INITIAL_BLACK_KING_POSITION: str = "40"
    INITIAL_WHITE_KING_POSITION: str = "47"

    def __init__(self) -> None:
        self.piece_positions: Dict[str, Piece] = self.get_start_piece_position()
        self.possible_castles: Dict[str, str] = {}
        self.possible_moves: List[str] = []
        self.black_king_position: str = self.INITIAL_BLACK_KING_POSITION
        self.white_king_position: str = self.INITIAL_WHITE_KING_POSITION
        self.en_passant_positions: Optional[Tuple[str, str]] = None
        self.board_state_counts: Dict[tuple, int] = {}

    def get_piece_positions(self, isStart: bool) -> Dict[str, str]:
        if isStart:
            return get_start_position
        
        return get_serialized_piece_positions

    # METHODS TO FIND MOVES #
    ''' Find all legal moves given the location of a piece '''
    def get_legal_moves(self, square: str) -> List[str]:
        all_possible_moves = []
        if isinstance(self.piece_positions[square], Pawn):
            en_passant_position = self.en_passant_positions[1] if self.en_passant_positions is not None else None
            all_possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions, en_passant_position)
        else:
            all_possible_moves = self.piece_positions[square].calculate_possible_moves(square, self.piece_positions)

        self.possible_moves = self.delete_invalid_moves(square, all_possible_moves)
        return self.add_castling(square)
    
    ''' Delete any illegal moves (moves that place own King in check) '''
    def delete_invalid_moves(self, square: str, possible_moves: List[str]) -> List[str]:
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
    def add_castling(self, square: str) -> List[str]:
        if not isinstance(self.piece_positions[square], King):
            return self.possible_moves
        
        self.possible_castles = self.piece_positions[square].handle_castling(square, self.piece_positions)
        if self.possible_castles:
            for key in self.possible_castles.keys():
                self.possible_moves.append(key)

        return self.possible_moves

    '''  Find the location of en_passant for the next move, if any '''
    def get_en_passant_location(self, start_square: str, destination_square: str) -> Optional[List[str]]:
        if isinstance(self.piece_positions[start_square], Pawn) and \
                      self.piece_positions[start_square].is_double_step(start_square[1], destination_square[1]):
            skipped_square = str(start_square[0]) + str(max(int(destination_square[1]), int(start_square[1])) - 1)
            return [destination_square, skipped_square]
        return None


    # METHODS TO HANDLE PIECE MOVEMENT #
    ''' method to move piece in the game '''
    def move(self, start_square: str, destination_square: str) -> Dict[str, Any]:
        self.piece_positions = self.perform_move(start_square, destination_square, False)

        pawn_can_promote = None
        if isinstance(self.piece_positions[destination_square], Pawn) and \
            self.piece_positions[destination_square].can_promote(destination_square):
            pawn_can_promote = destination_square

        position = self.get_serialized_piece_positions()
        self.update_board_state_count(position)
        game_state = self.get_game_state(self.piece_positions[destination_square].is_white, position)

        return { 
            "piecePositions":  self.get_serialized_piece_positions(),
            "pawnCanPromote": pawn_can_promote,
            "gameState": game_state
        }
    
    ''' method to temporarily perform a move and return the position of all pieces after movement
        if test_move is True there will be no changes to stored variables in the GameState class '''
    def perform_move(self, start_square: str, destination_square: str, test_move: bool = True) -> Dict[str, Piece]:
        piece_positions = self.piece_positions.copy()

        # set prevous double step to find possible en passants
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
    def update_piece_metadata(self, piece_positions: Dict[str, Piece], start_square: str, destination_square: str) -> None:
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
    def castle(self, castle_type: str, piece_positions: Dict[str, Piece]) -> Dict[str, Piece]:
        if castle_type == "shortWhite":
            piece_positions["57"] = piece_positions.pop("77")
        elif castle_type == "longWhite":
            piece_positions["37"] = piece_positions.pop("07")
        elif castle_type == "shortBlack":
            piece_positions["50"] = piece_positions.pop("70")
        elif castle_type == "longBlack":
            piece_positions["30"] = piece_positions.pop("00")

        return piece_positions
    
    def promote_pawn(self, pawn_location: str, promote_to: str) -> Dict[str, str]:
        piece_map = {
            "Queen": Queen,
            "Rook": Rook,
            "Bishop": Bishop,
            "Knight": Knight
        }
        if promote_to in piece_map:
            self.piece_positions[pawn_location] = piece_map[promote_to](self.piece_positions[pawn_location].is_white)
        return self.get_serialized_piece_positions()

    # GAME STATE METHODS #
    ''' return the state of the game '''
    def get_game_state(self, is_white: bool, position: Dict[str, str]) -> Optional[str]:
        if not self.has_legal_moves(is_white):
            if self.is_king_in_check(is_white):
                return "checkmate"
            else:
                return "stalemate"
        if self.is_draw_by_insufficient_material():
            return "insufficient material"
        # todo - three fold repititon state needs to be reset between games!
        if self.check_threefold_repetition(position):
            return "three-fold repetition"
        if self.is_king_in_check(is_white):
            return "check"

        return None
    
    def is_draw_by_insufficient_material(self) -> bool:
        if len(self.piece_positions) > 4:
            return False
        # if there is one bishop and one king per side it is a draw, any other combination of four pieces is not
        elif len(self.piece_positions) == 4:
            num_of_white_bishops = 0
            num_of_black_bishops = 0
            for piece in self.piece_positions.values():
                if isinstance(piece, Bishop):
                    if piece.is_white:
                        num_of_white_bishops += 1
                    else:
                        num_of_black_bishops += 1
            if num_of_black_bishops == 1 and num_of_black_bishops == 1:
                return True
        # if there are only 3 pieces all of which are a king, bishop or knight, it is a draw
        elif all(isinstance(piece, (King, Bishop, Knight)) for piece in self.piece_positions.values()):
            return True

        return False
    
    def update_board_state_count(self, position: Dict[str, str]) -> None:
        state = tuple(position)
        if state in self.board_state_counts:
            self.board_state_counts[state] += 1
        else:
            self.board_state_counts[state] = 1

    def check_threefold_repetition(self, position: Dict[str, str]) -> bool:
        state = tuple(position)
        return self.board_state_counts.get(state, 0) >= 3
    
    
    # UTILITY METHODS #
    ''' Construct an Object for with piece position as keys and piece name as values for client uptake '''
    def get_serialized_piece_positions(self) -> Dict[str, str]:
        serialized_positions = {}
        for position, piece in sorted(self.piece_positions.items()):
            serialized_positions[position] = piece.name

        return serialized_positions
        
    ''' Set/Reset the board to the starting position '''
    def get_start_position(self) -> Dict[str, str]:
        self.piece_positions = self.get_start_piece_position()
        return self.get_serialized_piece_positions()
    
    ''' Define the intial piece positions on the board '''
    def get_start_piece_position(self) -> Dict[str, Piece]:
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
    
    ''' return if the given king is in check'''
    def is_king_in_check(self, is_white: bool) -> bool:
        king = self.black_king_position if is_white else self.white_king_position
        return self.piece_positions[king].is_in_check(king, self.piece_positions)
    
    ''' calculate the given side has any legal moves'''
    def has_legal_moves(self, is_white: bool) -> bool:
        for piece in self.piece_positions:
            if self.piece_positions[piece].is_white is not is_white and self.get_legal_moves(piece):
                return True
                
        return False