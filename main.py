#%%
from chess import Move
from board.board_wrapper import BoardWrapper
from minmax import find_best_move 

state: BoardWrapper = BoardWrapper()
move: Move
move_uci: str

ai_player: bool = False
#%%
while not state.is_over():
    print(state)

    if ai_player:
        move = find_best_move(maximize=False, depth=2, state=state) 
    
    else: 
        move_uci = str(input('Your move (from UCI format): '))
        move = Move.from_uci(move_uci)
    
    state.make_move(move)
    print(move.uci())
    
    ai_player = not ai_player
        