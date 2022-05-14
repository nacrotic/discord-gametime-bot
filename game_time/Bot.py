import os

from discord import Intents
from discord.ext import commands

from game_time import TextUtils


class MyBot(commands.Bot):
    def __init__(self):
        default_intents = Intents.default()
        default_intents.members = True
        super().__init__(command_prefix="!", intents=default_intents)

    async def on_ready(self):
        print("on_ready bot")

    async def on_member_join(self, member):
        print("on_member_join " + member.display_name)
        general_channel = member.guild.system_channel
        if None != general_channel:
            welcome_message = os.getenv("welcome").replace(r'\n', '\n').format(name=member.display_name)
            message_part = TextUtils.split_message(welcome_message, 2000)
            for part in message_part:
                await general_channel.send(part)
