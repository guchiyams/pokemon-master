import player
from typing import List, Self, TypedDict

class GameState(TypedDict):
    player1: player.Player
    player2: player.Player
    turn_order: int

class Game:
    def __init__(self, player1: player.Player, player2: player.Player):   # player 2 will be AI
        self.player1: player1
        self.player2: player2
        self.turn_order = player1 \
                            if player1.pokemon_team[player1.active_pokemon_index].base_stats.speed > player2.pokemon_team[player2.active_pokemon_index].base_stats.speed \
                            else player2

    def run_game_loop(self):
        pass

    ### ===== GETTERS ===== ###
    # get current game state
    def get_game_state(self) -> dict:
        game_state = {
            "player1": self.player1,
            "player2": self.player2,
            "turn_order": self.turn_order
        }

        return game_state