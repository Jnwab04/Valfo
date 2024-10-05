import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
import discord
from discord import app_commands
from discord.ext import commands
from agents import Agents
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents = discord.Intents.all())

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        agents = Agents()
        print(synced)

        print(f'Logged on as {client.user}')
    except Exception as e:
        print(e)

@client.tree.command(name="help", description="bleh")
async def help(interaction):
    await interaction.response.send_message("HEYY")
@client.tree.command(name="bye", description="BLUUHH")
async def bye(interaction):
    embed = discord.Embed(title="Agents", description="here are the ageents", color=discord.Colour.purple())
    await interaction.response.send_message(embed = embed)
client.run(BOT_TOKEN)