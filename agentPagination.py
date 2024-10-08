import discord
from agents import Agents
class AgentPageView(discord.ui.View):
   current_page: int = 1
   sep: int = 5
   message: discord.Message = None  # Initialize message as None
   agentName : str
   agentClass : Agents

   async def send(self, ctx):
      # Send the initial message and assign it to self.message
      embed = self.create_embed(self.agentName)  # Display the first page
      self.message = await ctx.response.send_message(embed=embed, view=self)  # Embed with view

   def create_embed(self, name):
      print("in create embed")
      if self.current_page == 1:
        embed = self.agentClass.getAgentInfoEmbed(name = name)
      else:
         embed = self.agentClass.getAgentAbilityEmbed(agentname= name, num = self.current_page - 2)
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
      name = self.agentName
      print("in update Message")
      self.update_buttons()  # Update buttons first
      if self.message:
         # Edit the message with new embed data
         await self.message.edit(embed=self.create_embed(name), view=self)

   @discord.ui.button(label="Info", style=discord.ButtonStyle.primary)
   async def description_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 1
      await self.update_message()

   @discord.ui.button(label="A1", style=discord.ButtonStyle.grey)
   async def abilityone(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 2
      await self.update_message()

   @discord.ui.button(label="A2", style=discord.ButtonStyle.gray)
   async def abilitytwo(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 3
      await self.update_message()
   
   @discord.ui.button(label="A3", style=discord.ButtonStyle.grey)
   async def abilitythree(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 4
      await self.update_message()

   @discord.ui.button(label="Ult", style=discord.ButtonStyle.gray)
   async def ultimate(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 5
      await self.update_message()
   

