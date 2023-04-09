from typing import List, Optional

# TODO: avoid using this, do a wrapper
from chess import Move

from board.board_wrapper import BoardWrapper

def minimax(maximize: bool, depth: int, state: BoardWrapper) -> int:
    if depth == 0 or state.is_over():
        last_move: Move = state.get_last_move()
        return state.evaluate(last_move)
    
    scores: List[int] = []
    for move in state.get_possible_moves():
        state.make_move(move)
        scores.append(minimax(not maximize, depth-1, state))
        state.undo_move()

    return max(scores) if maximize else min(scores)

def find_best_move(maximize: bool, depth: int, state: BoardWrapper) -> Move:
    bestScore: int = -100000
    bestMove: Optional[Move] = None
    score: int = 0

    for move in state.get_possible_moves():
        state.make_move(move)
        score = minimax(maximize=maximize, depth=depth, state=state)
        state.undo_move()
        
        if score > bestScore:
            bestScore = score
            bestMove = move

    return bestMove
