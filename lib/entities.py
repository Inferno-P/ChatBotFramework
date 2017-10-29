class Entity:
    entityName = None
    domain = []
    currentValue = None

    def __init__(self):
        pass

    def __init__(self,name,domain):
        self.setName(name)
        self.setDomain(domain)

    def setName(self,name):
        self.entityName = name

    def setDomain(self,domain):
        self.domain = domain