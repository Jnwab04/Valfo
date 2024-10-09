import discord
from agents import Agents
class AgentPageView(discord.ui.View):
   current_page: int = 1
   message: discord.Message = None  # Initialize message as None
   agentName : str
   agentClass : Agents

   async def send(self, ctx):
      await ctx.response.defer()
      # Send the initial message and assign it to self.message
      embed = self.create_embed()
      self.message = await ctx.followup.send(embed=embed, view=self) #send initial message

   def create_embed(self):
      if self.current_page == 1:
        embed = self.agentClass.getAgentInfoEmbed(name = self.agentName)
      else:
         embed = self.agentClass.getAgentAbilityEmbed(agentname = self.agentName, num = self.current_page - 2)
      return embed
   
   def update_buttons(self):
      if self.current_page == 1:
         self.description_button.disabled = True
         self.abilityone.disabled = False
         self.abilitytwo.disabled = False
         self.abilitythree.disabled = False
         self.ultimate.disabled = False
      elif self.current_page == 2:
         self.description_button.disabled = False
         self.abilityone.disabled = True
         self.abilitytwo.disabled = False
         self.abilitythree.disabled = False
         self.ultimate.disabled = False
      elif self.current_page == 3:
         self.description_button.disabled = False
         self.abilityone.disabled = False
         self.abilitytwo.disabled = True
         self.abilitythree.disabled = False
         self.ultimate.disabled = False
      elif self.current_page == 4:
         self.description_button.disabled = False
         self.abilityone.disabled = False
         self.abilitytwo.disabled = False
         self.abilitythree.disabled = True
         self.ultimate.disabled = False
      else:
         self.description_button.disabled = False
         self.abilityone.disabled = False
         self.abilitytwo.disabled = False
         self.abilitythree.disabled = False
         self.ultimate.disabled = True

   async def update_message(self):
      self.update_buttons()  # Update buttons first
      if self.message:
         # Edit the message with new embed data
         await self.message.edit(embed=self.create_embed(name = self.agentName), view=self)

   @discord.ui.button(label="Info", style=discord.ButtonStyle.primary)
   async def description_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 1
      await self.update_message()

   @discord.ui.button(label="A1", style=discord.ButtonStyle.primary)
   async def abilityone(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 2
      await self.update_message()

   @discord.ui.button(label="A2", style=discord.ButtonStyle.primary)
   async def abilitytwo(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 3
      await self.update_message()
   
   @discord.ui.button(label="A3", style=discord.ButtonStyle.primary)
   async def abilitythree(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 4
      await self.update_message()

   @discord.ui.button(label="Ult", style=discord.ButtonStyle.primary)
   async def ultimate(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 5
      await self.update_message()
   

class AgentSelect(discord.ui.Select):
   def __init__(self, AgentClass):
      self.AgentClass = AgentClass
      options = []
      for agent in AgentClass.getAgents():
         options.append(discord.SelectOption(label = agent))
      placeholder = "Choose an agent"
      min_values= 1
      max_values= 1
      #creates dropdown menu of all the agents' names
      super().__init__(placeholder = placeholder, min_values = min_values, max_values= max_values, options=options)

   #callback checks when an option is selected
   async def callback(self, interaction):
      apv = AgentPageView()
      apv.agentName = self.values[0]
      apv.agentClass = self.AgentClass
      await interaction.message.edit(content = f"Agent Selected: {self.values[0]}", view = None)#delee dropdown menu
      await apv.send(interaction) #send the agents' page
   
class AgentSelectMenu(discord.ui.View):
   def __init__(self, aclass):
      super().__init__(timeout = 60)
      ags = AgentSelect(AgentClass=aclass)
      self.add_item(ags)
