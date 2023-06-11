from __future__ import annotations

from abc import ABC, abstractmethod
from random import random, choice

from player import Player
from settings import SELF_ENCOUNTER_NAME, DEATH_ENCOUNTER_NAME
from game_types import OptionalEncounterName, EncounterName


class BaseAction(ABC):
    @abstractmethod
    def execute(self, player: Player) -> OptionalEncounterName:
        ...


class DeathAction(BaseAction):
    def __init__(self, death_message: str):
        self._death_message = death_message

    def execute(self, player: Player) -> OptionalEncounterName:
        print(self._death_message)
        print("You are dead")
        return None


class ForageAction(BaseAction):
    def __init__(self, forage_target: str, probability: float):
        self._forage_target = forage_target
        self._probability = probability

    def execute(self, player: Player) -> OptionalEncounterName:
        if random() <= self._probability:
            print(f"You found a {self._forage_target}!")
        else:
            print("You found nothing.")
        return SELF_ENCOUNTER_NAME


class LookForEnemyAction(BaseAction):
    def __init__(self, enemy: str, probability: float, combat_encounter: EncounterName):
        self._enemy = enemy
        self._probability = probability
        self._combat_encounter = combat_encounter

    def execute(self, player: Player) -> OptionalEncounterName:
        if random() <= self._probability:
            print(f"You found a {self._enemy}")
            return self._combat_encounter
        else:
            print("You found nothing.")
            return SELF_ENCOUNTER_NAME


class QuitAction(BaseAction):
    def execute(self, player: Player) -> OptionalEncounterName:
        user_input = input("Are you sure? ")
        if user_input.strip().lower() in ["y", "yes"]:
            return None
        return SELF_ENCOUNTER_NAME


class GoToAction(BaseAction):
    def __init__(self, encounter: str):
        self._encounter = encounter

    def execute(self, player: Player) -> OptionalEncounterName:
        return self._encounter


class FightAction(BaseAction):
    def __init__(self, success_probability: float, victory_encounter: EncounterName):
        self._success_probability = success_probability
        self._victory_encounter = victory_encounter

    def execute(self, player: Player) -> OptionalEncounterName:
        if random() <= self._success_probability:
            return self._victory_encounter
        return DEATH_ENCOUNTER_NAME


class FleeAction(BaseAction):
    def __init__(self, success_probability: float, flee_encounters: list[EncounterName]):
        self._success_probability = success_probability
        self._flee_encounters = flee_encounters

    def execute(self, player: Player) -> OptionalEncounterName:
        if random() <= self._success_probability:
            return choice(self._flee_encounters)
        return SELF_ENCOUNTER_NAME
