from dataclasses import dataclass
from typing import Optional
from enum import Enum


class UnitType(str, Enum):
    SMC = "SMC"
    MMC = "MMC"
    SW = "SW"
    GUN = "Gun"
    VEHICLE = "Vehicle"


class Nationality(str, Enum):
    GERMAN = "German"
    AMERICAN = "American"
    BRITISH = "British"
    RUSSIAN = "Russian"
    JAPANESE = "Japanese"


class ExperienceLevel(str, Enum):
    ELITE = "E"
    FIRST_LINE = "1"
    SECOND_LINE = "2"
    GREEN = "G"
    CONSCRIPT = "C"
    USMC = "USMC"


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

    # Fire phase tracking
    has_fired_first_fire: bool = False
    has_fired_final_fire: bool = False
    is_cx: bool = False

    # Unit methods
    def break_unit(self):
        self.is_broken = True
        self.has_moved = False
        self.is_cx = False  # CX is removed when broken.

    def rally(self):
        self.is_broken = False
        self.has_moved = False

    def set_cx(self):
        self.is_cx = True

    def clear_cx(self):
        self.is_cx = False

    def mark_first_fire(self):
        self.has_fired_first_fire = True
        self.has_fired_final_fire = False

    def mark_final_fire(self):
        self.has_fired_first_fire = False
        self.has_fired_final_fire = True

    def reset_fire_markers(self):
        self.has_fired_first_fire = False
        self.has_fired_final_fire = False

    def pin(self):
        self.is_pinned = True

    def unpin(self):
        self.is_pinned = False

    def mark_moved(self):
        self.has_moved = True

    def reset_movement(self):
        self.has_moved = False

    def reset_all_status(self):
        self.has_moved = False
        self.has_fired_first_fire = False
        self.has_fired_final_fire = False
        self.is_pinned = False
        self.is_cx = False
