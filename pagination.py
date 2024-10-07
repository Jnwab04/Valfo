import discord

class Pageview(discord.ui.View):
   current_page: int = 1
   sep: int = 5
   message: discord.Message = None  # Initialize message as None
   data : list

   async def send(self, ctx):
      # Send the initial message and assign it to self.message
      embed = self.create_embed(self.data[:self.sep])  # Display the first page
      self.message = await ctx.response.send_message(embed=embed, view=self)  # Embed with view

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
      
      if self.current_page == (len(self.data) + self.sep - 1) // self.sep:
         self.last_page_button.disabled = True
         self.next_button.disabled = True
      else:
         self.last_page_button.disabled = False
         self.next_button.disabled = False
    

   async def update_message(self):
      from_item = (self.current_page - 1) * self.sep
      until_item = self.current_page * self.sep
      page_data = self.data[from_item:until_item]

      self.update_buttons()  # Update buttons first
      if self.message:
         # Edit the message with new embed data
         await self.message.edit(embed=self.create_embed(page_data), view=self)

   @discord.ui.button(label="|<", style=discord.ButtonStyle.primary)
   async def first_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.current_page = 1
      await self.update_message()
   

   @discord.ui.button(label="<", style=discord.ButtonStyle.primary)
   async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      if self.current_page > 1:
         self.current_page -= 1
      await self.update_message()

   @discord.ui.button(label=">", style=discord.ButtonStyle.primary)
   async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      total_pages = (len(self.data) + self.sep - 1) // self.sep
      if self.current_page < total_pages:
         self.current_page += 1
      await self.update_message()
      
   @discord.ui.button(label=">|", style=discord.ButtonStyle.primary)
   async def last_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      total_pages = (len(self.data) + self.sep - 1) // self.sep
      self.current_page = total_pages
      await self.update_message()
   
