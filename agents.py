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
    def getAgentInfo(self, name):
        name = (name[0].upper() + name[1:].lower()).strip()
        found = False
        agentDescription = None
        agentImage = None
        agentRole = None
        agentRoleThumbnail = None
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
                agentDescription = agent["description"]
                agentImage = agent["fullPortrait"]
                agentRoleThumbnail = agent["role"]["displayIcon"]
                agentRole = agent["role"]["displayName"]
                found = True
                break
        if not found:
            agentEmbed = discord.Embed(title = "Agent Not Found", type = "rich")
            return agentEmbed
        else:
            agentEmbed = discord.Embed(
                title= name,
                color = discord.Color.green(),
                type = 'rich',
                description = agentDescription
                )
            agentEmbed.set_image(url = agentImage)
            agentEmbed.set_footer(text=agentRole, icon_url= agentRoleThumbnail)

            return agentEmbed
