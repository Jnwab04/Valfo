import requests

class Buddies():
    __init_already__ = False

    def __init__(self):
        if Buddies.__init_already__ == False:
            Buddies.__init_already__ = True
            __url = "https://valorant-api.com/v1/buddies"
            __response = requests.get(__url).json()["data"]
            self.response = __response
        else:
            print ("Class already initialized")
    
    def printBuddies(self):
     for buddy in self.response:
        print (buddy["displayName"])


testca = Buddies()
testca.printBuddies()