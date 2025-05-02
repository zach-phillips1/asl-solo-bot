from dataclasses import dataclass
from typing import Optional
from enum import Enum

class UnitType(str, Enum):
    SMC = 'SMC'
    MMC = 'MMC'
    SW = 'SW'
    GUN = 'Gun'
    VEHICLE = 'Vehicle'

class Nationality(str, Enum):
    GERMAN = 'German'
    AMERICAN = 'American'
    BRITISH = 'British'
    RUSSIAN = 'Russian'
    JAPANESE = 'Japanese'

class ExperienceLevel(str, Enum):
    ELITE = 'E'
    FIRST_LINE = '1'
    SECOND_LINE = '2'
    GREEN = 'G'
    CONSCRIPT = 'C'
    USMC = 'USMC'

@dataclass
class Unit:
    name: str
    unit_type: UnitType
    nationality: Nationality

    # Optional stats
    firepower: Optional[int] = None
    range: Optional[int] = None
    morale: Optional[int] = None
    broken_morale: Optional[int] = None
    movement: Optional[int] = None
    smoke_exponent: Optional[int] = None
    can_assault_fire: Optional[bool] = None
    experience_level: Optional[ExperienceLevel] = None

    # Leader-specific
    is_leader: bool = False
    leadership_modifier: Optional[int] = None

    # Status flags
    is_broken: bool = False
    is_pinned: bool = False
    has_moved: bool = False
