from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config")
default_intents = Intents.default()
default_intents.members = True
bot = commands.Bot(command_prefix="!", intents=default_intents)


def connect():
    bot.run(os.getenv("token"))


@bot.event
async def on_ready():
    print("on_ready bot")


@bot.command(name="test")
async def test(ctx, number: int):
    print("on_message " + str(number))
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()


@bot.event
async def on_message(message):
    print("on_message " + message.content)


@bot.event
async def on_member_join(member):
    print("on_member_join " + member.display_name)
    general_channel = bot.get_channel(os.getenv("channel"))
    await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")



connect()
