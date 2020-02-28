class Greetings:
    def __init__(self):
        self.welcomeMsg = "Hello world"

    def getWelcomeMsg(self):
        return self.welcomeMsg

g1 = Greetings ()
print g1.getWelcomeMsg()
