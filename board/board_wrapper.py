from typing import Dict, List, Optional
from chess import Board, IllegalMoveError, Move, PieceType, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING



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

    def get_possible_sorted_moves(self) -> List[Move]:
        return self._sort_moves()

    def make_move(self, move: Move) -> None:
        if not self.board.is_legal(move):
            IllegalMoveError(f"Illegal move: {move.uci()}!")
        
        self.board.push(move)

    def undo_move(self) -> Move:
        return self.board.pop()
    
    def get_last_move(self) -> Move:
        return self.board.peek()

    def _sort_moves(self) -> List[Move]:
        moves: List[Move] = self.board.legal_moves

        pieces: List[Optional[PieceType]] = [
            self.board.piece_type_at(move.to_square) 
            for move in moves
        ]

        moves = sorted(
            zip(moves, pieces),
            key=lambda x: -1 * float('inf') if x[1] is None else x[1],
            reverse=True
        )

        return map(lambda x: x[0], moves)
    
    def evaluate_state(self, player: bool) -> int:
        total_score: int = 0
        self_score: int
        opponent_score: int

        for piece, score in PIECE_SCORES.items():
            self_score = len(self.board.pieces(piece_type=piece, color=player)) * score
            opponent_score = len(self.board.pieces(piece_type=piece, color=(not player))) * score * -1

            total_score += (self_score + opponent_score)

        return total_score
    
    def __str__(self) -> str:
        return str(self.board)