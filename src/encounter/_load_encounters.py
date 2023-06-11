from __future__ import annotations

from action import ForageAction, GoToAction, LookForEnemyAction
from encounter._action_factories import make_combat_action
from encounter._encounter import Encounter, EncounterAction
from game_types import EncounterName


def load_encounters() -> dict[EncounterName, Encounter]:
    encounters = [
        Encounter(
            name="edge_of_woods",
            description="You are standing next to the forest.",
            actions=[
                EncounterAction("f", "[F]orage for radishes", ForageAction("radish", 0.5)),
                EncounterAction("e", "[E]nter the forest", GoToAction("in_the_woods")),
            ],
        ),
        Encounter(
            name="in_the_woods",
            description="You are standing among very tall and very old oak trees. "
            "There is little vegetation under your feet, but a lot of crunchy leaves.",
            actions=[
                EncounterAction(
                    "l",
                    "[L]ook for dropbears",
                    LookForEnemyAction("dropbear", 0.25, EncounterName("combat_Dropbear")),
                ),
                EncounterAction("w", "[W]alk out of the forest", GoToAction("edge_of_woods")),
            ],
        ),
        make_combat_action("Dropbear", EncounterName("in_the_woods"), [EncounterName("edge_of_woods")]),
    ]

    return {e.name: e for e in encounters}
