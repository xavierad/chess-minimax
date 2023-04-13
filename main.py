#%%
from chess import Move
from board.board_wrapper import BoardWrapper
from minmax import find_best_move 

ai_player: bool = True

state: BoardWrapper = BoardWrapper('3r4/pR2N3/2pkb3/5p2/8/2B5/qP3PPP/4R1K1 w - - 1 0', white_to_play=True)
# state: BoardWrapper = BoardWrapper('2r3k1/p4p2/3Rp2p/1p2P1pK/8/1P4P1/P3Q2P/1q6 b - - 0 1', white_to_play=False)
move: Move
move_uci: str

#%%
while not state.is_over():
    print(state)

    if ai_player:
        move = find_best_move(state=state, depth=4) 
    
    else: 
        # move_uci = str(input('\nYour move (from UCI notation): '))
        # move = Move.from_uci(move_uci)
        move = find_best_move(state=state, depth=4) 
    
    state.make_move(move)
    print(move.uci())
    
    ai_player = not ai_player
        