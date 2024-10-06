import discord

class Pageview(discord.ui.View):
   current_page: int = 1
   sep: int = 5
   message: discord.Message = None  # Initialize message as None

   async def send(self, ctx):
      # Send the initial message and assign it to self.message
      self.message = await ctx.response.send_message(view=self)
      await self.update_message(self.data[:self.sep])

   def create_embed(self, data):
     embed = discord.Embed(title="test")
     for item in data:
        embed.add_field(name=item, value=item, inline=False)
     return embed
   
   def update_buttons(self):
      if self.current_page == 1:
         self.first_page_button.disabled = True
         self.previous_button.disabled = True
      else:
         self.first_page_button.disabled = False
         self.previous_button.disabled = False
    

   async def update_message(self, data):
      # Check if self.message is initialized
      if self.message:
         await self.message.edit(embed=self.create_embed(data), view=self)

   @discord.ui.button(label="|<", style=discord.ButtonStyle.primary)
   async def first_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 1
      until_item = self.current_page * self.sep
      await self.update_message(self.data[:until_item])

   @discord.ui.button(label="<", style=discord.ButtonStyle.primary)
   async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page -= 1
      until_item = self.current_page * self.sep
      from_item = until_item - self.sep
      await self.update_message(self.data[from_item:until_item])

   @discord.ui.button(label=">", style=discord.ButtonStyle.primary)
   async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page += 1
      until_item = self.current_page * self.sep
      from_item = until_item - self.sep
      await self.update_message(self.data[from_item:until_item])

   @discord.ui.button(label=">|", style=discord.ButtonStyle.primary)
   async def last_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = int(len(self.data) / self.sep) + 1
      until_item = self.current_page * self.sep
      from_item = until_item - self.sep
      await self.update_message(self.data[from_item:])
