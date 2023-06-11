from __future__ import annotations

from dataclasses import dataclass

from action import BaseAction


@dataclass
class EncounterAction:
    letter: str
    prompt: str
    action: BaseAction


@dataclass
class Encounter:
    name: str
    description: str
    actions: list[EncounterAction]
