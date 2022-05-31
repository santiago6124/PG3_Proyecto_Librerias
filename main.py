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


@bot.command(name="ayuda_graphind", help="Indica como usar el comando !graphind")
async def help_graphind(ctx):
    response = f"El comando graphind se utiliza de la siguiente manera: !graphind <ticker> <timefr> <limite> <indicador>"
    await ctx.send(response)


@bot.command(name="graphind", help="Comando para graficar indicadores")
async def graphind(ctx, ticker, timefr, limite, indicador):
    graph.rqst_graph_ind(ticker, timefr, int(limite), int(indicador))
    await ctx.send(file=discord.File("grafico.png"))
    try:
        os.remove("grafico.png")
    except FileNotFoundError:
        pass



bot.run(TOKEN)