from typing import List

import pytest
from board.puzzle import Puzzle


@pytest.mark.parametrize(
    'fen, white_to_play, moves_to_mate, depth, solution',
    [
        (
            '3r4/pR2N3/2pkb3/5p2/8/2B5/qP3PPP/4R1K1 w - - 1 0', True, 3, 4, ['c3e5', 'd6c5', 'e1c1', 'e6c4', 'b2b4']
        ),
    ]  
)
def test_puzzles(fen: str, white_to_play: bool, moves_to_mate: int, depth: int, solution: List[str]) -> None:
    board: Puzzle = Puzzle(fen=fen, white_to_play=white_to_play, moves_to_mate=moves_to_mate, depth=depth)
    assert board.solve() == solution