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
    
    def getAgentImage(self, name : str):
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
                return agent["fullPortrait"]
        return None
    def getAgentRole(self, name : str):
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
                return agent["role"]["displayName"]
        return None
    def getAgentDescription(self, name : str):
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
                return agent["description"]
        return None
    def getAgentRoleThumbnail(self, name : str):
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
                return agent["role"]["displayIcon"]
        return None
    def getAgentInfo(self, name):
        name = (name[0].upper() + name[1:].lower()).strip()
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
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
                description = self.getAgentDescription(name = name)
                )
            agentEmbed.set_image(url = self.getAgentImage(name = name))
            agentEmbed.set_footer(text=self.getAgentRole(name = name), icon_url= self.getAgentRoleThumbnail(name = name))

            return agentEmbed
