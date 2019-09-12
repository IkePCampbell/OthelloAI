class Player:
    def __init__(self,name,color):
        self.playerName = name
        self.tokenColor = color

    def getMove(self):
        print("What would you like to do:")
        #give options for either rules or quitting.
        aX = int(input("Enter a X coordinate for your "+self.tokenColor+": "))
        aY = int(input("Enter a Y coordinate for your "+self.tokenColor+": "))
        #Need to sanative these pieces
        return aX, aY
