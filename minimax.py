def minimax(maximize: bool, board) -> int:
    if board.is_terminal():
        if board.state() == 'draw':
            return 0
        else:
            return 10 if board.won()