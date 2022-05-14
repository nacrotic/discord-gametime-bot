import locale
import os
import time

import dateparser
from discord.ext import commands
from dotenv import load_dotenv

from game_time.Bot import MyBot
from game_time.Emoji import Emoji

load_dotenv(dotenv_path="config")
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')

bot = MyBot()

"""
Commande discord.
Supprime {number} messages en plus de la commande.
"""


@bot.command(name="clean")
async def clean(ctx, number: int):
    print("clean " + str(number))
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()


"""
Commande discord.
Planifie {number} prochaine seance.
"""


@bot.command(name="plan")
async def plan(ctx: commands.context, date_string: str):
    print("plan " + date_string)
    date = dateparser.parse(date_string + " Z")
    invite = await ctx.channel.send(date.strftime('%d %B'))
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
