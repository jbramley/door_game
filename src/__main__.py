from __future__ import annotations

from random import seed

from action import QuitAction
from encounter import EncounterAction, Encounter, load_encounters
from settings import SELF_ENCOUNTER_NAME, START_ENCOUNTER_NAME, DEATH_ENCOUNTER_NAME

QUIT_ENCOUNTER = EncounterAction("q", "[Q]uit game", QuitAction())

seed()
encounters = load_encounters()
previous_encounter = None
current_encounter = encounters[START_ENCOUNTER_NAME]


def get_user_action(encounter: Encounter) -> EncounterAction:
    print("\nWhat would you like to do now?")
    action_map = {}
    for a in encounter.actions + [QUIT_ENCOUNTER]:
        action_map[a.letter] = a
        print(a.prompt)

    action = None
    while action is None:
        choice = input("> ")
        action = action_map.get(choice.strip().lower())
        if action is None:
            print("I don't understand.")
    return action


while current_encounter:
    if current_encounter != previous_encounter:
        print(current_encounter.description)
    previous_encounter = current_encounter

    user_action = get_user_action(current_encounter)

    next_encounter_name = user_action.action.execute()
    if next_encounter_name is None:
        current_encounter = None
    elif next_encounter_name == DEATH_ENCOUNTER_NAME:
        print("You have died.")
        break
    elif next_encounter_name != SELF_ENCOUNTER_NAME:
        try:
            current_encounter = encounters[next_encounter_name]
        except KeyError:
            print(
                f"Error: {previous_encounter.name} has an action {user_action.prompt} "
                f"that references an invalid encounter: {next_encounter_name}"
            )
            break
