from dataclasses import dataclass


@dataclass
class Player:
    name: str
    max_mp: int
    curr_mp: int
    max_hp: int
    curr_hp: int
