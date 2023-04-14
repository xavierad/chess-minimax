from typing import List

from chess import Move
from board.board_wrapper import BoardWrapper
from minimax import find_best_move


class Puzzle:
    def __init__(self, fen: str, white_to_play: bool, moves_to_mate: int, depth: int) -> None:
        self.fen = fen
        self.turn = white_to_play
        self.moves_to_mate = moves_to_mate
        self.depth = depth
        self.board: BoardWrapper = BoardWrapper(state=fen, white_to_play=white_to_play)

    def solve(self) -> List[str]:
        moves: List[str] = []
        move: Move

        print(self.board)

        while not self.board.is_over() and  (len(moves) < (self.moves_to_mate * 2)):

            # no needed to check who is playing, the computer will player against itself
            move = find_best_move(state=self.board, depth=self.depth) 
            self.board.make_move(move)
            print(move.uci())
            print(self.board)

            moves.append(move.uci())
        
        return moves
    
