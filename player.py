class Player:
    def __init__(self,name,color):
        self.playerName = name
        self.tokenColor = color

    def getMove(self):
        print("What would you like to do:")
        #give options for either rules or quitting.
        aX = input("Enter a X coordinate for your "+self.tokenColor+": ")
        aY = input("Enter a Y coordinate for your "+self.tokenColor+": ")
        while aX.isdigit() == False or int(aX) >=8:
            aX = input("Your X Token is not valid, please enter a X coordinate for your "+self.tokenColor+": ")
        while aY.isdigit() == False or int(aY) >=8:
            aY = input("Your Y Token is not valid, please enter a Y coordinate for your "+self.tokenColor+": ")
        #Need to sanative these pieces
        return int(aX), int(aY)
