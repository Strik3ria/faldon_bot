from discord.ext import commands

from .utils.send import send


class Overview(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="command_help", aliases=["commands", "command"])
    async def commands(self, ctx):
        response = (
            "The following commands are available currently:\n\n!reset\n"
            "!repair\n!vendors\n!spell spell_name\n!religion religion_name\n"
            "!suffix suffix_name\n!prefix prefix_name\n!drop creature_name"
        )
        await send(ctx, response)


def setup(bot):
    bot.add_cog(Overview(bot))
