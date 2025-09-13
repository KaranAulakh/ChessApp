from typing import Dict, List, Optional

class Piece:
    name: Optional[str] = None
    is_white: Optional[bool] = None

    def __init__(self, name: str, is_white: bool) -> None:
        self.name, self.is_white = name, is_white

    def is_valid_piece_at_location(self, x: int, y: int, piece_positions: Dict[str, 'Piece'], typeName: str, canBeEmpty: bool = False) -> bool:
        if (0 <= x <= 7) and (0 <= y <= 7):
            if canBeEmpty and str(x) + str(y) not in piece_positions:
                return True
            if str(x) + str(y) in piece_positions and typeName in piece_positions[str(x) + str(y)].name:
                return True
        return False
    
    def calculate_possible_moves(self) -> None:
        NotImplementedError("Subclass Must Implement this Method")