import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
import discord
from discord import app_commands
from discord.ext import commands
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents = discord.Intents.all())

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()

        print(f"Synced: {len(synced)} commands")
        print(f"{synced}")
        print(f'Logged on as {client.user}')
    except Exception as e:
        print(e)

@client.tree.command(name="first_command", description="bleh")
async def first_command(interaction):
    await interaction.response.send_message("HEYY")
@client.tree.command(name="bye", description="BLUUHH")
async def first_command(interaction):
    await interaction.response.send_message("BYEEE")
client.run(BOT_TOKEN)