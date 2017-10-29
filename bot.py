class Bot:
    inputToIntent = {}
    botName = None

    def __init__(self):
        pass

    def __init__(self,name):
        self.botName = name

    def mapIntentToInput(self,intent,userInput):
        self.inputToIntent[intent] = userInput

    def build(self):
        pass

    def test(self,inputString):
        for intent in self.inputToIntent.keys():
            if inputString in self.inputToIntent[intent].inputList:
                #By name entity recognition : we get entity names from user input
                intent.entities[0].currentValue = "A R Rahman"
                intent.entities[1].currentValue = "Pop"
                intent.executeAction()