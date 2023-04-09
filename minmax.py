from typing import List, Optional

# TODO: avoid using this, do a wrapper
from chess import Move

from board.board_wrapper import BoardWrapper

def minimax_alpha_beta(maximize: bool, depth: int, state: BoardWrapper, alpha: int=-10000, beta: int=10000) -> int:
    if depth == 0 or state.is_over():
        if maximize:
            return -state.evaluate()  
        else:
            return state.evaluate() 
    
    score: int = -10000 if maximize else 10000
    sub_score: int
    for move in state.get_possible_moves():
        state.make_move(move)
        if state.get_piece_captured() is not None:
            if maximize:
                score = -state.evaluate()  
            else:
                score = state.evaluate() 
    
            state.undo_move()
            break

        sub_score = minimax_alpha_beta(
            maximize=(not maximize), 
            depth=depth-1, 
            state=state, 
            alpha=alpha, 
            beta=beta
        )
        if maximize: 
            score = max(score, sub_score)
            alpha = max(alpha, sub_score)
        else:
            score = min(score, sub_score)
            beta = min(beta, sub_score)

        state.undo_move()

        if beta <= alpha:
            break

    return score

def find_best_move(maximize: bool, depth: int, state: BoardWrapper) -> Move:
    bestScore: int = -100000 if maximize else 100000
    bestMove: Optional[Move] = None
    score: int = 0

    for move in state.get_possible_moves():
        state.make_move(move)
        score = minimax_alpha_beta(maximize=maximize, depth=depth, state=state)
        state.undo_move()
        
        if maximize and score > bestScore:
            bestScore = score
            bestMove = move
        elif not maximize and score < bestScore:
            bestScore = score
            bestMove = move
        print(score)
    print(bestScore)
    return bestMove
