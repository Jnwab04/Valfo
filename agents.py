import requests
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