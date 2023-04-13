#%%
from chess import Move
from board.board_wrapper import BoardWrapper
from minmax import find_best_move 

state: BoardWrapper = BoardWrapper()
move: Move
move_uci: str

# If False, then ai_player play for blacks
ai_player: bool = False
#%%
while not state.is_over():
    print(state)

    if ai_player:
        move = find_best_move(maximize=(not ai_player), depth=4, state=state) 
    
    else: 
        move_uci = str(input('\nYour move (from UCI notation): '))
        move = Move.from_uci(move_uci)
    
    state.make_move(move)
    print(move.uci())
    
    ai_player = not ai_player
        