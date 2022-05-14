import locale
import os
import time

import dateparser
from discord.ext import commands
from dotenv import load_dotenv

from game_time import Checks
from game_time.Bot import MyBot
from game_time.Emoji import Emoji

load_dotenv(dotenv_path="config")
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')

bot = MyBot()


@bot.command(name="clean")
@commands.check(Checks.is_author_in_allowed_group)
async def clean(ctx: commands.context, number: int):
    """Supprime les messages les plus récent

    :param ctx: contexte de la commande (fourni par le framwork)
    :param number: nombre de message a supprimer en plus du message pour la commande (passé par l'utilisateur)
    """
    print("clean " + str(number))
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()


@bot.command(name="plan")
@commands.check(Checks.is_author_in_allowed_group)
async def plan(ctx: commands.context, date_string: str):
    """Planifie une prochaine seance

    :param ctx: contexte de la commande (fourni par le framwork)
    :param date_string: date de la prochaine seance (passée par l'utilisateur)
    """
    print("plan " + date_string)
    date = dateparser.parse(date_string + " Z")
    invite = await ctx.channel.send(date.strftime('%d %B %Y'))
    time.sleep(0.1)
    await invite.add_reaction(Emoji.x.value)
    await invite.add_reaction(Emoji.question.value)
    await invite.add_reaction(Emoji.thumbsup.value)
    await invite.add_reaction(Emoji.v.value)
    await invite.add_reaction(Emoji.love_you_gesture.value)
    await invite.add_reaction(Emoji.four_leaf_clover.value)
    await invite.add_reaction(Emoji.hand_splayed.value)
    await ctx.message.delete()


bot.run(os.getenv("token"))
