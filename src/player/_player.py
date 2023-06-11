from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    max_mp: int
    curr_mp: int = field(init=False)
    max_hp: int
    curr_hp: int = field(init=False)

    def __post_init__(self):
        self.curr_hp = self.max_hp
        self.curr_mp = self.max_mp
