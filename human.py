class Human:
    name = None
    height = None
    hair_color = None

    def __init__(self,name=None,height=None,hair_color=None):
        self.name = str(name)
        self.hair_color = str(hair_color)
        self.height = float(height)

    def getName(self):
        return self.name

    def getHairColor(self):
        return self.hair_color
    
    def getHeight(self):
        return self.height

    def setName(self, name):
        self.name = str(name)

    def setHairColor(self, color):
        self.hair_color = str(color)

    def setHeight(self, height):
        self.height = float(height)


