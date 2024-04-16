from typing import List
import pokemon
import move

class Player:
    def __init__(self, name: str, pokemon_team: List[pokemon.Pokemon], starting_pokemon_index: int):
        self.name = name
        self.pokemon_team = pokemon_team
        self.active_pokemon_index = starting_pokemon_index

    def switch_active_pokemon(self, pokemon_index):
        self.active_pokemon_index = pokemon_index

    ### ===== GETTERS ===== ###
    # get active pokemon's moves
    def get_active_pokemon_moves(self) -> List[move.Move]:
        active_pokemon = self.pokemon_team[self.active_pokemon_index]
        return active_pokemon.get_moves()