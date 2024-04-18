from typing import List
import pokemon
import move

class Player:
    def __init__(self, pokemon_team: List[pokemon.Pokemon], starting_pokemon_index: int):
        self.pokemon_team = pokemon_team
        self.active_pokemon_index = starting_pokemon_index

    def apply_next_move(self, move_index: int = -1, opponent_pokemon: pokemon.Pokemon = None, sw_pokemon_index: int = -1, switch: bool = False) -> None:
        # TODO: add other moves (e.g., defend, heal, etc.)
        # for now player can only switch pokemon or attack with active pokemon
        if switch:
            self.switch_active_pokemon(sw_pokemon_index)
            return
        
        active_pokemon = self.pokemon_team[self.active_pokemon_index]
        active_pokemon.attack(move_index, opponent_pokemon)
        return

    # set active pokemon to new pokemon
    def switch_active_pokemon(self, pokemon_index):
        self.active_pokemon_index = pokemon_index

    ### ===== GETTERS ===== ###
    # get active pokemon's moves
    def get_active_pokemon_moves(self) -> List[move.Move]:
        active_pokemon = self.pokemon_team[self.active_pokemon_index]
        return active_pokemon.get_moves()