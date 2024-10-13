import requests
import discord

class Gamemodes():
    __init_already__ = False
    def __init__(self):
        if not Gamemodes.__init_already__:
            Gamemodes.__init_already__ = True
            __url = "https://valorant-api.com/v1/gamemodes"
            __response = requests.get(__url).json()["data"]
            self.response = __response

    def getGameModeImage(self, name : str):
        for mode in self.response:
            if  mode["displayName"] == name:
                return mode["listViewIconTall"]
    
    def getGameModeIcon(self, name: str):
        for mode in self.response:
            if mode["displayName"] == name:
                return mode["displayIcon"]
            
    def getGameModeTime(self, name: str):
        for mode in self.response:
            if mode["displayName"] == name:
                if mode["duration"] == None:
                    return "Varies"
                else:
                    return mode["duration"]
            
    def getGameDescription(self, name : str):
        for mode in self.response:
            if mode["displayName"] == name:
                return mode["description"]

    def getGamemodeEmbed(self, name: str):
        if name.isupper() == False:
           name = name.capitalize()
        for mode in self.response:
            if str(mode["displayName"]).lower().strip() == name.lower().strip():
                found = True
                break
        if not found:
            modeEmbed = discord.Embed(title = "Mode Not Found", type = "rich")
            return modeEmbed
        else:
            modeEmbed = discord.Embed(
                title= mode["displayName"],
                color = discord.Color.dark_teal(),
                type = 'rich',
                description = self.getGameDescription(name = name)
                )
            modeEmbed.add_field(name="Mode Duration", value= self.getGameModeTime(name = mode["displayName"]), inline=False)
            modeEmbed.set_image(url = self.getGameModeImage(name = mode["displayName"] ))
            modeEmbed.set_thumbnail(url= self.getGameModeIcon(name = mode["displayName"]))
            return modeEmbed