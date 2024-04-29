import json
import discord
import os
from discord.ext import commands

with open("./json/config.json", "r") as f:
    config = json.load(f)


class MyBot(commands.Bot):
    def __init__(self):

        super().__init__(
            command_prefix=f"{config['additional']['prefix']}",
            intents=discord.Intents.all(),
            application_id=config['additional']['application_id']
        )

    async def setup_hook(self):

        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        await bot.tree.sync()

    async def on_ready(self):
        print('Logged in!')


bot = MyBot()
bot.run(config['tokens']['discord_token'])
