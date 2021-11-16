religions = {
    "sagittarius": {
        "description": (
            "Sagitarius worshipers rely on constitution for "
            "damage and health/energy regeneration. They commonly "
            "use melee weapons or ranged shooting weapons like "
            "the bow. They worship the all powerful Catbert."
        ),
        "stat_bonuses": [
            "constitution",
            "stamina",
        ],
        "attribute_bonuses": [
            "physical damage",
            "melee crit",
            "berserk movement speed",
            "long berserk uptime",
        ],
        "resources": ["uses energy to pay spell and skill costs."],
        "spells": ["antimagic", "bless", "empower", "Greater Heal", "prayer"],
    },
    "druid": {
        "description": (
            "Druid worshippers rely on intellect for damage and magic for "
            "mana regeneration. They are considered best used as pure mages "
            "and use staves or weapon/shield combinations. They worship the "
            "almighty Gaia."
        ),
        "stat_bonuses": ["intellect", "magic", "constitution"],
        "attribute_bonuses": [
            "spell crit",
            "spell damage",
            "pets have no timer",
            "pets have no hunger",
            "bonus lightning/cold damage",
        ],
        "resources": [
            "uses mana to pay for spells",
            "energy to pay for skill costs",
        ],
        "spells": [
            "energy bolt",
            "blizzard",
            "chain lightning",
            "summon wolves",
            "earthquake",
            "banish",
        ],
    },
    "undead": {
        "description": (
            "Undead worshippers rely on intellect for damage and magic for "
            "mana regeneration. They are considered best used as battle mages "
            "and use staves or weapon/shield combinations. They worship The "
            "Idol."
        ),
        "stat_bonuses": ["intellect", "magic", "strength"],
        "attribute_bonuses": [
            "fire damage",
            "poison damage",
            "fire damage fro melee attacks",
            "have no hunger",
            "health, energy, and mana regeneration",
        ],
        "resources": [
            "uses mana to pay for spells",
            "energy to pay for skill costs",
        ],
        "spells": [
            "flamestrike",
            "flaming arrow",
            "apocalypse",
            "raise dead",
            "summon spiders",
            "decrepify",
        ],
    },
    "paladin": {
        "description": (
            "Paladin worshippers rely on strength for damage"
            ". They are considered best used as pure warrior "
            "and use two handed or weapon/shield combinations. "
            "They worship the Light."
        ),
        "stat_bonuses": ["strength", "constitution", "defense"],
        "attribute_bonuses": [
            "armor class",
            "buffed blocking",
            "resist all",
            "HP increase at higher ranks",
            "overall movement speed increase",
        ],
        "resources": [
            "uses mana to pay for spells",
            "energy to pay for skill costs",
        ],
        "spells": [
            "healing wind",
            "holy armor",
            "exorcism",
            "holy lightning",
            "holy strike",
            "empower",
        ],
    },
}
