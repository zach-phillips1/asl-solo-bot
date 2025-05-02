import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from unit import Unit, UnitType, Nationality, ExperienceLevel

def test_basic_unit_creation():
    squad = Unit(
        name="4-6-7",
        unit_type=UnitType.MMC,
        nationality=Nationality.GERMAN,
        firepower=4,
        range=6,
        morale=7,
        broken_morale=7,
        movement=4,
        experience_level=ExperienceLevel.FIRST_LINE
    )

    assert squad.name == "4-6-7"
    assert squad.firepower == 4
    assert squad.is_broken is False
    assert squad.experience_level == ExperienceLevel.FIRST_LINE
