from typing import NewType

EncounterName = NewType('EncounterName', str)
OptionalEncounterName = EncounterName | None
