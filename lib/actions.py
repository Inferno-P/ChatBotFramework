class Action:
    method = None
    actionName = None

    def __init__(self):
        pass;

    def __init__(self,name,method):
        self.setActionName(name)
        self.setMethod(method)

    def setMethod(self,method):
        self.method = method

    def setActionName(self,name):
        self.actionName = name
