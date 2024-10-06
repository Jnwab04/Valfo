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
agents = Agents()
@client.event
async def on_ready():
    try:
        synced = await client.tree.sync(guild = discord.Object(id = 1291847955963449374)) 
        
        print(synced)
        print(f'Logged on as {client.user}')
    except Exception as e:
        print(e)

@client.tree.command(name="help", description="Provides a list of commands (synced to our guild only)", guild = discord.Object(id = 1291847955963449374))
async def help(interaction):
    await interaction.response.send_message("HEYY")

@client.tree.command(name="agentinfo", description="Provides information on every agent (synced to our guild only)", guild = discord.Object(id = 1291847955963449374))
async def agentinfo(interaction, agent: str):
    embed = agents.getAgent(name = agent)
    #embed.add_field(name = "test3", value = "value2", inline = False)
    await interaction.response.send_message(embed = embed)

@client.tree.command(name="shutdown", description="force shut down the bot (synced to our guild only)" , guild = discord.Object(id = 1291847955963449374))
async def shutdown(interaction):
    exit()
client.run(BOT_TOKEN)