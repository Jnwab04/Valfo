import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
import discord
from discord import app_commands
from discord.ext import commands
from agents import Agents
from buddies import Buddy
from pagination import Pageview
from agentMenus import AgentPageView, AgentSelectMenu
from gamemodes import Gamemodes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GUILD = 1291847955963449374

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents = discord.Intents.all())
agents = Agents()
buddys = Buddy()
gmode = Gamemodes()
@client.event
async def on_ready():
    try:
        synced = await client.tree.sync(guild = discord.Object(id = 1291847955963449374)) 
        
        print(synced)
        print(f'Logged on as {client.user}')
    except Exception as e:
        print(e)

@client.tree.command(name="help", description="Provides a list of commands (synced to our guild only)", guild = discord.Object(id = GUILD))
async def help(interaction):
    await interaction.response.send_message("HEYY")

@client.tree.command(name="agentinfo", description="Provides information on every agent (synced to our guild only)", guild = discord.Object(id = GUILD))
async def agentinfo(interaction, agent: str = None):
    if agent != None:        
        agentpaginateview = AgentPageView()
        agentpaginateview.agentClass = agents   
        agentpaginateview.agentName = agent
        await agentpaginateview.send(interaction)
    else:   
        selectMenu = await interaction.response.send_message("Select An Agent", view = AgentSelectMenu(aclass = agents))
@client.tree.command(name="getbuddy", description="Provides information on all buddies (synced to our guild only)", guild = discord.Object(id = GUILD))
async def buddies(interaction, buddy:str):
    b_embed = buddys.getBuddies(buddy)
    await interaction.response.send_message(embed = b_embed)

@client.tree.command(name="paginate", description="make page (synced to our guild only)", guild = discord.Object(id = GUILD))
async def paginate(ctx):
    data = range(1,15)
    paginateview = Pageview()
    paginateview.data = list(data)
    await paginateview.send(ctx)
@client.tree.command(name="gamemodes",description="Provides information on the avalible game modes in valorant", guild = discord.Object(id = GUILD) ) 
async def gamemodes(interaction, gamemode: str):
    g_embed =  gmode.getGamemodeEmbed(gamemode)
    await interaction.response.send_message(embed = g_embed)

@client.tree.command(name="shutdown", description="force shut down the bot (synced to our guild only)" , guild = discord.Object(id = GUILD))
async def shutdown(interaction):
    exit()
client.run(BOT_TOKEN)