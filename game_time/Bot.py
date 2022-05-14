import os

import discord.abc
from discord import Intents
from discord.ext import commands

from game_time import TextUtils


class MyBot(commands.Bot):
    def __init__(self):
        default_intents = Intents.default()
        default_intents.members = True
        super().__init__(command_prefix="!", intents=default_intents)

    async def on_ready(self):
        """Indication que le bot est bien demarré

        :return: Coroutine tel que défini par le framwork discord.py
        """
        print("on_ready bot")

    async def on_member_join(self, member: discord.Member):
        """Message d'accueil personnalisé

        :param member: les informations du membre nouvellement arrivé
        :return: Coroutine tel que défini par le framwork discord.py
        """
        print("on_member_join " + member.display_name)
        general_channel = member.guild.system_channel
        guild_chanel = member.guild.channels
        welcome_chan: discord.abc.GuildChannel = general_channel
        for channel in guild_chanel:
            if channel.name == 'vélo':
                welcome_chan = channel
                break
        if general_channel is not None:
            welcome_message = os.getenv("welcome") \
                .replace(r'\n', '\n') \
                .format(name=member.mention, chan=welcome_chan.mention)
            message_part = TextUtils.split_message(welcome_message, 2000)
            for part in message_part:
                await general_channel.send(part)
