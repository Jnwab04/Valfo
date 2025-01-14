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
    def getAgentIcon(self, name : str):
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == name:
                return agent["displayIcon"]
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
    
    def getAgentAbility(self, agentname : str, abilitynum : int):
        abilityname = None
        abilitydesc = None
        abilityicon = None
        for agent in self.response:
            if agent["isPlayableCharacter"] and agent["displayName"] == agentname:
                abilityname = agent["abilities"][abilitynum]["displayName"]
                abilitydesc = agent["abilities"][abilitynum]["description"]
                abilityicon = agent["abilities"][abilitynum]["displayIcon"]
                return [abilityname, abilitydesc, abilityicon]
        return None
        

    def getAgentAbilityEmbed(self, agentname : str, num : int):
        agentname = (agentname[0].upper() + agentname[1:].lower()).strip()
        abilityInfo = self.getAgentAbility(agentname = agentname, abilitynum=num)
        if abilityInfo == None:
            abilityEmbed = discord.Embed(title = "Error", type = "rich")
            return abilityEmbed
        else:
            abilityName = abilityInfo[0]
            abilityDesc = abilityInfo[1]
            abilityIcon = abilityInfo[2]
            abilityEmbed = discord.Embed(
                title = f"Ability {num + 1}: {abilityName}",
                color = discord.Color.blue(),
                description=abilityDesc)
            if (num + 1) >= 4:
                abilityEmbed.title = f"Ultimate: {abilityName}"
            abilityEmbed.set_image(url = abilityIcon)
            abilityEmbed.set_footer(icon_url= self.getAgentIcon(name=agentname), text=agentname)
            return abilityEmbed
        
    def getAgentInfoEmbed(self, name):
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
                color = discord.Color.dark_teal(),
                type = 'rich',
                description = self.getAgentDescription(name = name)
                )
            agentEmbed.set_image(url = self.getAgentImage(name = name))
            agentEmbed.set_footer(text=self.getAgentRole(name = name), icon_url= self.getAgentRoleThumbnail(name = name))

            return agentEmbed
    def getAgents(self):
        temp = []
        for agent in self.response:
            if agent["isPlayableCharacter"]:
                temp.append(agent["displayName"])
        return temp