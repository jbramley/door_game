from action import FightAction, FleeAction
from encounter._encounter import Encounter, EncounterAction
from game_types import EncounterName


def make_combat_action(enemy: str, victory_encounter: EncounterName, flee_encounters: list[EncounterName]) -> Encounter:
    return Encounter(
        name=f"combat_{enemy}",
        description=f"You have entered combat with a {enemy}",
        actions=[
            EncounterAction("a", f"[A]ttack {enemy}", FightAction(0.5, victory_encounter)),
            EncounterAction("f", "[F]lee the fight", FleeAction(0.25, flee_encounters)),
        ],
    )
