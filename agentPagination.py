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
      embed = self.create_embed(self.agentName)
      self.message = await ctx.followup.send(embed=embed, view=self) #send initial message

   def create_embed(self, name):
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
   

