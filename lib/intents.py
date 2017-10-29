class Intent:
    intentName = None
    entities = [] # list of entities
    action = None # action

    def __init__(self):
        pass

    def __init__(self,name,entities,action):
        self.intentName = name
        self.entities = entities
        self.action = action

    def setName(self,name):
        self.intentName = name

    def executeAction(self,):
        self.action.method(self.entities[0].currentValue,self.entities[1].currentValue)
