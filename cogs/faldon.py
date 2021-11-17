from discord.ext import commands

from .utils.send import send
from .utils.proper_case import proper_case
from .utils.spells import spells, get_spells_by_type, sort_spells_by_start
from .utils.prefixes import prefixes
from .utils.suffixes import suffixes
from .utils.find_suffix import find_suffix
from .utils.religions import religions
from .utils.drops import drops


class Faldon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="spell", aliases=["spells"])
    async def spell(self, ctx, *spell):
        if len(spell) == 0:
            response = (
                "Make sure to give me a spell to look up for you. "
                "ex. '!spell medusas stare'"
            )
            await send(ctx, response)
            return

        spell = [proper_case(s) for s in spell]
        spell = str.join(" ", spell)

        response = ""

        try:
            selected_spell = spells[spell.lower()]
            response = (
                f"{spell} is a spell of the {selected_spell['type']} skill"
                " type.\nYou can start casting this "
                f"spell at skill level {selected_spell['skill_begin']}.\n"
                "It will stop fizzling at skill level "
                f"{selected_spell['fizzle_stop']}."
            )
        except KeyError as error:

            try:
                response = (
                    f"The following spells are available for {spell}:\n\n"
                    f"ex: spell name: starts - fizzle end\n\n"
                )

                unsorted_spells = get_spells_by_type(spell)
                sorted_spells = sort_spells_by_start(unsorted_spells)

                for spell in sorted_spells:
                    response += (
                        f"{spell}:\t{sorted_spells[spell]['skill_begin']} - "
                        f"{sorted_spells[spell]['fizzle_stop']}\n"
                    )
            except ValueError as error:
                response = "The spell or spell type you are looking for was not found."
                print(f"spell: {error} is probably not a spell or spell type.")

        await send(ctx, response)

    @commands.command(
        name="vendors",
        aliases=["vend", "vendor", "sell", "traders", "npc", "npcs", "trade"],
    )
    async def vendors(self, ctx):
        response = (
            "Most items can be sold to Rick or Kyra. Both are "
            "located in southern Valour in their own respective buildings."
        )
        await send(ctx, response)

    @commands.command(name="repair", aliases=["itemrepair", "repairs"])
    async def repair(self, ctx):
        response = (
            "Items can be repaired for 500gp/dura at the Valour Castle. "
            "Look for Shady Tony or Tim the Enchanter in particular."
        )

        await send(ctx, response)

    @commands.command(
        name="stat-reset", aliases=["reset", "resetstat", "statreset"]
    )
    async def stat_reset(self, ctx):
        response = (
            "Stat resets are currently free from Dr. Reset. They can be "
            "found in Midgaurd."
        )
        await send(ctx, response)

    @commands.command(name="prefix", aliases=["pre", "prefixes"])
    async def prefix(self, ctx, *prefix_name):
        if len(prefix_name) == 0:
            response = (
                "Make sure to give me a prefix to look up for you. "
                "ex. '!prefix mystic'"
            )
            await send(ctx, response)
            return

        prefix_name = [proper_case(p) for p in prefix_name]
        prefix_name = str.join(" ", prefix_name)

        try:
            selected_prefix = prefixes[prefix_name.lower().replace("'", "")]
            stats = selected_prefix["stats"]
            formatted_stats = ""

            for stat in stats.keys():
                formatted_stats += f"{proper_case(stat)}: +{stats[stat]}\n"

            response = (
                f"The '{prefix_name}' prefix adds the following "
                f"attributes to an item:\n\n{formatted_stats}"
            )
        except KeyError:
            response = "The prefix you are looking for could not be found."
            print(f"prefix: {prefix_name} is probably not a prefix.")

        await send(ctx, response)

    @commands.command(name="suffix", aliases=["suf", "suffixes"])
    async def suffix(self, ctx, *suffix_name):
        if len(suffix_name) == 0:
            response = (
                "Make sure to give me a suffix to look up for you. "
                "ex. '!suffix of the jaguar' or '!suffix jaguar'"
            )
            await send(ctx, response)
            return

        suffix_name = [proper_case(s) for s in suffix_name]
        suffix_name = str.join(" ", suffix_name)

        try:
            suffix_full_name = find_suffix(suffix_name)
            selected_suffix = suffixes[suffix_full_name]
            if selected_suffix == "Not found":
                raise KeyError(suffix_full_name)

            stats = selected_suffix["stats"]
            formatted_stats = ""

            for stat in stats.keys():
                formatted_stats += f"{proper_case(stat)}: +{stats[stat]}\n"

            response = (
                f"The '{suffix_full_name}' suffix adds the following "
                f"attributes to an item:\n\n{formatted_stats}"
            )
        except KeyError:
            response = "The suffix you are looking for could not be found."
            print(f"suffix: {suffix_name} is probably not a suffix.")

        await send(ctx, response)

    @commands.command(name="religion", aliases=["religions"])
    async def religion(self, ctx, religion_name):
        if len(religion_name.split(" ")) > 1 or len(religion_name) == 0:
            response = (
                "Please enter the name of a religion. (sagittarius, "
                "druid, undead, paladin)"
            )
            await send(ctx, response)
            return

        try:
            selected_religion = religions[religion_name]
        except KeyError:
            response = "The religion you are looking for could not be found."
            selected_religion = None
            print(f"religion: {religion_name} is probably not a religion.")

        if selected_religion is not None:
            response = f"{selected_religion['description']}\n\nSpells:\n"
            num_of_spells = len(selected_religion["spells"])

            for i in range(0, num_of_spells):
                response += f"{selected_religion['spells'][i]}\n"

                if i == num_of_spells - 1:
                    response += "\n"

            response += (
                f"{proper_case(religion_name)} receives bonuses to "
                "these stats:\n"
            )
            num_of_stat_bonuses = len(selected_religion["stat_bonuses"])

            for i in range(0, num_of_stat_bonuses):
                response += f"{selected_religion['stat_bonuses'][i]}\n"

                if i == num_of_stat_bonuses - 1:
                    response += "\n"

            response += (
                f"{proper_case(religion_name)} receives bonuses to "
                "these attributes:\n"
            )
            num_of_attribute_bonuses = len(
                selected_religion["attribute_bonuses"]
            )

            for i in range(0, num_of_attribute_bonuses):
                response += f"{selected_religion['attribute_bonuses'][i]}\n"

                if i == num_of_attribute_bonuses - 1:
                    response += "\n"

            response += f"{proper_case(religion_name)} uses these resources:\n"
            num_of_resources = len(selected_religion["resources"])

            for i in range(0, num_of_resources):
                response += f"{selected_religion['resources'][i]}\n"

        else:
            await send(
                ctx, "The religion you are looking for could not be found."
            )
            return

        await send(ctx, response)

    @commands.command(name="drop", aliases=["drops", "loot"])
    async def drop(self, ctx, *creature_name):
        creature_name = str.join(" ", creature_name).title()
        try:
            selected_creature = drops[creature_name]
        except KeyError:
            response = "The creature you are looking for could not be found."
            await send(ctx, response)

        response = f"{creature_name} drops the following items:\n\n"
        for item in selected_creature.keys():
            response += (f"{item}: {selected_creature[item]['quantity']}, "
                         f"{selected_creature[item]['rate']}\n")

            if len(response) > 1800:
                await send(ctx, response)
                response = ""

        await send(ctx, response)

    @commands.command()
    async def test(self, ctx, *spell_type):
        if len(spell_type) == 0:
            response = (
                "Make sure to give me a spell type to look up for you. "
                "ex. '!spell elemental magics'"
            )
            await send(ctx, response)
            return

        spell_type = " ".join(spell_type).title()

        response = (
            f"The following spells are available for {spell_type}:\n\n"
            f"ex: spell name: starts - fizzle end\n\n"
        )

        unsorted_spells = get_spells_by_type(spell_type)
        sorted_spells = sort_spells_by_start(unsorted_spells)

        for spell in sorted_spells:
            response += (
                f"{spell}:\t{sorted_spells[spell]['skill_begin']} - "
                f"{sorted_spells[spell]['fizzle_stop']}\n"
            )

        await send(ctx, response)


def setup(bot):
    bot.add_cog(Faldon(bot))
