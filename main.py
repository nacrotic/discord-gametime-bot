from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config")


class Bot(commands.Bot):
    def __init__(self):
        default_intents = Intents.default()
        default_intents.members = True
        super().__init__(command_prefix="!", intents=default_intents)

    async def on_ready(self):
        print("on_ready bot")

    async def on_message(self, message):
        print("on_message " + message.content)

    async def on_member_join(self, member):
        print("on_member_join " + member.display_name)
        general_channel = bot.get_channel(int(os.getenv("channel")))
        await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

    @commands.Bot.command(name="test")
    async def test(self, ctx, number: int):
        print("on_message " + str(number))
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()


bot = Bot()
bot.run(os.getenv("token"))