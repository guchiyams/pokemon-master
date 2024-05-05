from game import *
import json

with open('./data.json', 'r') as f:
    _game_state = json.load(f)
    # print(game_state)

import time
start_time = time.time()

# ai = _game_state['ai']
# ai_pokemon_team = ai['pokemon_team']
# ai_active_pokemon = ai_pokemon_team[ai['active_pokemon_index']]

# player = _game_state['player']
# player_pokemon_team = player['pokemon_team']
# player_active_pokemon = player_pokemon_team[player['active_pokemon_index']]

# print(checkWinner(game_state))

# GAME LOOP
while (checkWinner(_game_state) != 1):
    # get turn order
    turn_order = _game_state['turn_order']
    print(turn_order)

    # if turn order is 'ai'
    if turn_order == 'ai':
        moves = getMoveset(_game_state)
        best_move = moves[bestMove(_game_state)[0]]
        print(moves[bestMove(_game_state)[0]])

        # perform best move
        if 'switch' in best_move:
            _game_state['ai']['active_pokemon_index'] = best_move['switch']
        elif 'move' in best_move:
            attack(_game_state, bestMove(_game_state)[0])
    # if turn order is 'player'
    else:
        moves = getMoveset(_game_state)
        random_move = moves[floor(random() * len(moves))]
        print(random_move)

        # perform random move
        if 'switch' in random_move:
            _game_state['player']['active_pokemon_index'] = random_move['switch']
        elif 'move' in random_move:
            attack(_game_state, floor(random() * len(moves)))

    _game_state['turn_order'] = 'ai' if _game_state['turn_order'] == 'player' else 'player'

    pprint(_game_state)

# game_state = bestMove(game_state, top_n=5)

print("--- %s seconds ---" % (time.time() - start_time))
