from typing import Dict, List, Optional
from chess import Board, IllegalMoveError, Move, Piece, PieceType, Square, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING


PIECE_SCORES: Dict[str, int] = {
    PAWN: 1,
    KNIGHT: 3,
    BISHOP: 3,
    ROOK: 5,
    QUEEN: 8,
    KING: 10
}

class BoardWrapper:
    def __init__(self) -> None:
        self.board: Board = Board()

    def is_draw(self) -> bool:
        return self.board.is_insufficient_material() or self.board.is_stalemate()

    def is_checkmate(self) -> bool:
        return self.board.is_checkmate()

    def is_over(self) -> bool:
        return self.is_draw() or self.is_checkmate()
    
    def get_possible_moves(self) -> List[Move]:
        return self.board.legal_moves
    
    def _get_score(self, move: Move) -> int:
        capture_square: Square = move.to_square
        piece_capture: PieceType = self.board.piece_type_at(capture_square)
        if piece_capture:
            return PIECE_SCORES[piece_capture] 
        
        self.board.push(move)
        if self.board.is_checkmate():
            self.undo_move()
            return 1000
        
        self.undo_move()
        return 0

    def make_move(self, move: Move) -> None:
        if not self.board.is_legal(move):
            raise IllegalMoveError(f"Illegal move: {move.uci()}!")
        
        self.board.push(move)

    def undo_move(self) -> None:
        self.board.pop()
    
    def get_last_move(self) -> Move:
        return self.board.peek()

    def evaluate(self, move: Move) -> int:
        return self._get_score(move)
    
    def __str__(self) -> str:
        return str(self.board)