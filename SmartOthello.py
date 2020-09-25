import numpy as np
class Smart():
    def __init__(self,name,color,model):
        self.playerName = name
        self.tokenColor = color
        self.brain = model
    def getMove(self, *args):
        choices = []
        store = {}
        for spot in range(len(args[0])):  
            store[spot] = [args[0][spot]]
        for key in store:
            situation = np.array(store[key])
            result = self.brain.think(situation)
            for i in result:
                store[key].append(i[0])
        final = []
        for key in store:
            final.append([store[key][1],store[key][0]])
        final.sort(reverse=True)
        aX,aY = final[0][1]
        return int(aY), int(aX)
        
        
        
        