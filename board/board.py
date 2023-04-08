from typing import Dict, List
from chess import Board, Move, PieceType, Square, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING


PIECE_SCORES: Dict[str, int] = {
    PAWN: 1,
    KNIGHT: 3,
    BISHOP: 3,
    ROOK: 5,
    QUEEN: 8,
    KING:10
}

class Board:
    def __init__(self) -> None:
        self.board: Board = Board()

    def is_over(self) -> bool:
        return self.board.is_over()
    
    def is_draw(self) -> bool:
        return self.board.is_draw()
    
    def get_moves(self) -> List[Move]:
        return self.board.legal_moves()
    
    def get_score(self, move: Move) -> int:
        capture_square: Square = move.to_square
        piece_capture: PieceType = self.board.piece_type_at(capture_square)
        return PIECE_SCORES[piece_capture]
