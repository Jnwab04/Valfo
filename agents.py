import requests
import discord
class Agents():
    __init_already__ = False
    def __init__(self):
        if not Agents.__init_already__:
            Agents.__init_already__ = True
            __url = "https://valorant-api.com/v1/agents"
            __response = requests.get(__url).json()["data"]
            self.response = __response
    def printAgents(self):
        for agent in self.response:
            if agent["isPlayableCharacter"]:
                print(agent["displayName"])
    def getAgent(self, name):
        #capitalize first name to access API easier
        name = (name[0].upper() + name[1:].lower()).strip()
        agentDescription = None
        agentImage = None
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
                agentDescription = agent["description"]
                agentImage = agent["fullPortrait"]
                break
        agentEmbed = discord.Embed(
            title= name,
            color = discord.Color.green(),
            type = 'rich',
            description = agentDescription
            )
        agentEmbed.set_image(url = agentImage)

        return agentEmbed
