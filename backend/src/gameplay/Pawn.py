from typing import Dict, List, Optional
from gameplay.Piece import Piece

class Pawn(Piece):
    promotion_row: int
    start_row: int
    advance_increment: int
    en_passant_move: Optional[str] = None

    def __init__(self, is_white: bool) -> None:
        super().__init__("WhitePawn" if is_white else "BlackPawn", is_white)
        self.start_row = 6 if is_white else 1
        self.promotion_row = 0 if is_white else 7
        self.advance_increment = -1 if is_white else 1

    def calculate_possible_moves(self, square: str, piece_positions: Dict[str, Piece], en_passant: Optional[str]) -> List[str]:
        possible_moves = []
        x, y = int(square[0]), int(square[1]) + self.advance_increment
        opponent = "Black" if self.is_white else "White"


        # Check for captures
        for dx in [-1, 1]:
            if self.is_valid_piece_at_location(x + dx, y, piece_positions, opponent, False) or en_passant == str(x + dx) + str(y):
                possible_moves.append(str(x + dx) + str(y))
        
        # Add single space advance or return if blocked
        if (str(x) + str(y) not in piece_positions and 0 <= y <= 7):
            possible_moves.append(str(x) + str(y))
            # Add double space advance if available
            y += self.advance_increment
            if (self.start_row == int(square[1]) and str(x) + str(y) not in piece_positions and 0 <= y <= 7):
                possible_moves.append(str(x) + str(y))

        return possible_moves
    
    def is_double_step(self, start_row: str, destination_row: str) -> bool:
        return int(start_row) == self.start_row and int(destination_row) == self.start_row + self.advance_increment + self.advance_increment
        
    def can_promote(self, square: str) -> bool:
        return self.promotion_row == int(square[1])
    