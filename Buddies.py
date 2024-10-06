import requests
import discord
from pagination import Pageview

class Buddy():
    __init_already__ = False

    def __init__(self):
        if Buddy.__init_already__ == False:
            Buddy.__init_already__ = True
            __url = "https://valorant-api.com/v1/buddies"
            __response = requests.get(__url).json()["data"]
            self.response = __response
        else:
            print ("Class already initialized")
    
    def getBuddies(self, name):
        name = name
        found = False
        buddyImage = None
        for buddy in self.response:
            if buddy["displayName"] == name:
                buddyImage = buddy["displayIcon"]
                found= True
                break
        if not found:
            buddyEmbed = discord.Embed(title = "Buddy Not Found", type = "rich")
            return buddyEmbed
        else:
            buddyEmbed = discord.Embed(title = name, color= discord.Color.red())
            buddyEmbed.set_thumbnail(url= buddyImage)
            return buddyEmbed