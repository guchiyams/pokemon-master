import move
from typing import List, TypedDict

class BaseStats(TypedDict):
    # TODO: define BaseStats
    pass

class Pokemon:
    species: str
    level: int
    moves: List[move.Move]
    base_stats: BaseStats
    current_hp: int
    

    def __init__(self, species: str, level: int, moves: List[move.Move], base_stats: BaseStats):
        self.species = ""
        self.level = level
        self.moves = moves
        self.base_stats = base_stats
        self.current_hp = base_stats.hp     # assuming base stats has hp value
        self.status_conditions = ""         # not sure how we would implement status

    ### ===== GETTERS ===== ###
    # get pokemon moves
    def get_moves(self) -> List[move.Move]:
        return self.moves