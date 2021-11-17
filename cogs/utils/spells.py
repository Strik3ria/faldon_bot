from enum import Enum


class SpellType(Enum):
    WIZARDRY = "Wizardry"
    THAUMATURGY = "Thaumaturgy"
    NECROMANCY = "Necromancy"
    ELEMENTALMAGICS = "Elemental Magics"


def sort_spells_by_start(unsorted_spells):
    sorted_spells = dict(sorted(
        unsorted_spells.items(),
        key=lambda spell: spell[1]['skill_begin']
    ))

    return sorted_spells


def get_spells_by_type(spell_type):
    result = {}

    for spell in spells:
        if spells[spell]['type'] == SpellType(spell_type.title()).value:
            result[spell] = spells[spell]

    return result


spells = {
    "fireball": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 0,
        "fizzle_stop": 20,
    },
    "icebolt": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 20,
        "fizzle_stop": 45,
    },
    "flaming arrow": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 40,
        "fizzle_stop": 60,
    },
    "blizzard": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 55,
        "fizzle_stop": 75,
    },
    "flame strike": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 70,
        "fizzle_stop": 90,
    },
    "wraith": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 80,
        "fizzle_stop": 95,
    },
    "banshees wail": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 90,
        "fizzle_stop": 105,
    },
    "firewall": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 100,
        "fizzle_stop": 115,
    },
    "ice nova": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 115,
        "fizzle_stop": 135,
    },
    "earthquake": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 130,
        "fizzle_stop": 150,
    },
    "charged bolt": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 145,
        "fizzle_stop": 165,
    },
    "meteor storm": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 160,
        "fizzle_stop": 180,
    },
    "decrepify": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 175,
        "fizzle_stop": 205,
    },
    "chaos bolt": {
        "type": SpellType.ELEMENTALMAGICS.value,
        "skill_begin": 200,
        "fizzle_stop": 210,
    },
    "poison cloud": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 1,
        "fizzle_stop": 25,
    },
    "dark touch": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 20,
        "fizzle_stop": 45,
    },
    "burning rain": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 45,
        "fizzle_stop": 65,
    },
    "summon slimes": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 65,
        "fizzle_stop": 90,
    },
    "cowardice": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 75,
        "fizzle_stop": 90,
    },
    "death darts": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 90,
        "fizzle_stop": 105,
    },
    "curse": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 100,
        "fizzle_stop": 115,
    },
    "weaken": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 120,
        "fizzle_stop": 135,
    },
    "raise dead": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 130,
        "fizzle_stop": 150,
    },
    "slowed actions": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 145,
        "fizzle_stop": 165,
    },
    "summon spiders": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 160,
        "fizzle_stop": 180,
    },
    "apocalypse": {
        "type": SpellType.NECROMANCY.value,
        "skill_begin": 175,
        "fizzle_stop": 210,
    },
    "holy aura": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 0,
        "fizzle_stop": 15,
    },
    "lesser heal": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 15,
        "fizzle_stop": 30,
    },
    "shield": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 30,
        "fizzle_stop": 45,
    },
    "hermes speed": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 25,
        "fizzle_stop": 45,
    },
    "cure poison": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 40,
        "fizzle_stop": 55,
    },
    "healing wind": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 25,
        "fizzle_stop": 55,
    },
    "nature shield": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 25,
        "fizzle_stop": 55,
    },
    "empower": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 50,
        "fizzle_stop": 65,
    },
    "antimagic": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 60,
        "fizzle_stop": 75,
    },
    "holy armour": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 70,
        "fizzle_stop": 85,
    },
    "holy strike": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 100,
        "fizzle_stop": 115,
    },
    "true seeing": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 110,
        "fizzle_stop": 125,
    },
    "bless": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 75,
        "fizzle_stop": 125,
    },
    "greater heal": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 120,
        "fizzle_stop": 135,
    },
    "holy lightning": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 130,
        "fizzle_stop": 160,
    },
    "exorcism": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 140,
        "fizzle_stop": 185,
    },
    "banish": {
        "type": SpellType.THAUMATURGY.value,
        "skill_begin": 175,
        "fizzle_stop": 205,
    },
    "magic missile": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 1,
        "fizzle_stop": 20,
    },
    "night sight": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 10,
        "fizzle_stop": 30,
    },
    "lightning": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 10,
        "fizzle_stop": 30,
    },
    "illusionary menace": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 30,
        "fizzle_stop": 45,
    },
    "chain lightning": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 40,
        "fizzle_stop": 60,
    },
    "town portal": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 50,
        "fizzle_stop": 70,
    },
    "nova": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 65,
        "fizzle_stop": 85,
    },
    "flash": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 75,
        "fizzle_stop": 90,
    },
    "summon wolf": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 85,
        "fizzle_stop": 105,
    },
    "polymorph": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 95,
        "fizzle_stop": 115,
    },
    "energy bolt": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 115,
        "fizzle_stop": 135,
    },
    "medusas stare": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 130,
        "fizzle_stop": 145,
    },
    "mind blast": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 135,
        "fizzle_stop": 155,
    },
    "teleport": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 150,
        "fizzle_stop": 170,
    },
    "ethereal gate": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 160,
        "fizzle_stop": 180,
    },
    "nauseate": {
        "type": SpellType.WIZARDRY.value,
        "skill_begin": 175,
        "fizzle_stop": 205,
    },
}
