import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from isort import file

import ta as graph
import alert

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f"{bot.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})\n"
        "El bot está listo para usarse!"
    )


@bot.command(name="test", help="Comando de prueba")
async def test(ctx):
    response = "El bot esta conectado!"
    await ctx.send(response)


@bot.command(name="luukinho", help="Una foto del mejor 9 del mundo")
async def luuk(ctx):
    await ctx.send(file=discord.File("pfp.jpeg"))


bot.run(TOKEN)
