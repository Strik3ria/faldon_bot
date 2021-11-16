import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

cogs = ["cogs.faldon", "cogs.overview"]


class FaldonBot(commands.AutoShardedBot):
    def __init__(self, command_prefix='!'):
        commands.Bot.__init__(self, command_prefix=command_prefix)

    def run(self):
        for cog in cogs:
            self.load_extension(cog)

        super().run(TOKEN)


if __name__ == "__main__":
    print("please run from launcher.py")
