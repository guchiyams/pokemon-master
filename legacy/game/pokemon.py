import move
from typing import List, TypedDict, Self

class BaseStats(TypedDict):
    # TODO: define BaseStats
    hp: int
    level: int
    speed: int
    moves: List[move.Move]
    # defense: int
    # armour: int


class Pokemon:
    species: str                # pokemon species name
    level: int = 1              # pokemon level – default to 1
    moves: List[move.Move]
    base_stats: BaseStats
    current_hp: int

    def __init__(self, species: str, base_stats: BaseStats):
        self.species = species
        self.level = base_stats.level
        self.base_stats = base_stats
        self.current_hp = base_stats.hp
        self.moves = base_stats.moves
        self.status_conditions = ""

    def attack(self, move_index: int, opponent_pokemon: Self) -> None:
        # TODO: compute formula for attack on opponent (consider defense, armour, etc.)
        # for now, subtract move's power from opponent hp
        attack_move = self.moves[move_index]
        opponent_pokemon.current_hp = opponent_pokemon.current_hp - attack_move.power \
                                        if opponent_pokemon.current_hp - attack_move.power > 0 \
                                        else 0
        return    

    ### ===== GETTERS ===== ###
    # get pokemon moves
    def get_moves(self) -> List[move.Move]:
        return self.moves