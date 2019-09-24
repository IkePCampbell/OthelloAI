import random
class Rando:
    def __init__(self,name,color):
        self.playerName = name
        self.tokenColor = color

    def getMove(self):
        aX = random.randint(0,7)
        aY = random.randint(0,7)
        return aX, aY
