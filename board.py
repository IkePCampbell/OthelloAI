class Board:
    def __init__(self):
        self.board = [
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','B','W','x','x','x'],
        ['x','x','x','W','B','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],   
        ['x','x','x','x','x','x','x','x'],     ]

    def canMove(self,acolor):
        moveList = []
        for row in range(len(self.board)):
            for piece in range(len(self.board[row])):
                if self.board[row][piece] == acolor:
                    moveList+=self.moves(piece,row,acolor,'get')
        if len(moveList) != 0:
            moveList = self.cleanList(moveList)
            return moveList, True
        else:
            return moveList, False        
    def moves(self,aX,aY,acolor,mode):
        enemy = ""
        if acolor == "B":
            enemy = "W"
        else:
            enemy = "B"
        '''
        Moves is going to be used in both FINDING the potential spots to flip 
        and the end pieces that we will flip
        aX,aY = X,Y Coordinate of the piece
        aColor = B or W
        additive: 
            When we look for an X we want to give a spot of an extra index to actually reach the spot
            when we look for a color piece we dont want to add anything to it
        '''
        possibleMoves = []
##################################################################################
        leftOf = self.board[aY][:aX]
        leftOf.reverse()
        if mode == 'get':
            keepGoing,spot = self.keepGoingMoves(leftOf,'x',enemy)
            if keepGoing:
                possibleMoves.append([aY,aX-(spot+1)])
        else:
            keepGoing,spot = self.keepGoingMoves(leftOf,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY,aX-(spot),acolor)

        rightOf = self.board[aY][aX+1:] #have to add 1 to not include the original
        if mode == 'get':
            keepGoing,spot= self.keepGoingMoves(rightOf,'x',enemy)
            if keepGoing:
                possibleMoves.append([aY,aX+(spot+1)])
        else:
            keepGoing,spot= self.keepGoingMoves(rightOf,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY,aX+(spot),acolor)

        aboveOf = []
        for i in range(0,aY): #get all possible spots above you
            aboveOf.append(self.board[i][aX])
        aboveOf.reverse()
        if mode == 'get':
            keepGoing,spot  = self.keepGoingMoves(aboveOf,'x',enemy)
            if keepGoing:
                possibleMoves.append([aY-(spot+1),aX])
        else:
            keepGoing,spot = self.keepGoingMoves(aboveOf,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY-(spot),aX,acolor)
##################################################################################
        belowOf = []
        for i in range(aY+1,len(self.board)): #get all possible spots above you
            belowOf.append(self.board[i][aX])
        if mode == 'get':
            keepGoing,spot = self.keepGoingMoves(belowOf,'x',enemy)
            if keepGoing:
                possibleMoves.append([aY+(spot+1),aX]) 
        else:
            keepGoing,spot = self.keepGoingMoves(belowOf,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY+(spot),aX,acolor)
#####################################################333
        diagnolUpRight = []
        tmpX = aX
        tmpY = aY
        while (tmpY > -1) and tmpX < 8: #get all possible spots above you
            try:
                diagnolUpRight.append(self.board[tmpY][tmpX])
            except IndexError:
                pass
            tmpX+=1 #because we keep subtracting we eventually run out of room for the list
            tmpY-=1 
        if len(diagnolUpRight) > 0:
            diagnolUpRight.pop(0) #Get rid of the piece we started at
        if mode == 'get':
            keepGoing,spot = self.keepGoingMoves(diagnolUpRight,'x',enemy)
            if keepGoing:
                possibleMoves.append([aY-(spot+1),aX+(spot+1)])
        else:
            keepGoing,spot = self.keepGoingMoves(diagnolUpRight,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY-(spot),aX+(spot),acolor)
#####################################################333
        diagnolUpLeft = []
        tmpX = aX
        for i in range(aY,-1,-1): #get all possible spots above you
            diagnolUpLeft.append(self.board[i][tmpX])
            tmpX= (tmpX-1)% 8 #because we keep subtracting we eventually run out of room for the list
        if len(diagnolUpLeft) > 0:
            diagnolUpLeft.pop(0) #Get rid of the piece we started at
        if mode == 'get':
            keepGoing, spot = self.keepGoingMoves(diagnolUpLeft, 'x',enemy)
            if keepGoing:
                possibleMoves.append([aY-(spot+1),aX-(spot+1)])
        else:
            keepGoing, spot = self.keepGoingMoves(diagnolUpLeft,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY-(spot),aX-(spot),acolor)

####################################################333
        diagnolDownRight = []
        tmpX = aX
        tmpY = aY
        while (tmpY <  8) and tmpX < 8: #get all possible spots above you
            try:
                diagnolDownRight.append(self.board[tmpY][tmpX])
            except IndexError:
                pass
            tmpX+=1 #because we keep subtracting we eventually run out of room for the list
            tmpY+=1 
        if len(diagnolDownRight) > 0:
            diagnolDownRight.pop(0) #Get rid of the piece we started at
        if mode == 'get':
            keepGoing,spot = self.keepGoingMoves(diagnolDownRight, 'x',enemy)
            if keepGoing:
                possibleMoves.append([aY+(spot+1),aX+(spot+1)]) 
        else:
            keepGoing,spot = self.keepGoingMoves(diagnolDownRight,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY+(spot),aX+(spot),acolor)
#####################################################333
        diagnolDownLeft = []
        tmpX = aX
        tmpY = aY
        while tmpY < 8 and tmpX > -1:
            try:
                diagnolDownLeft.append(self.board[tmpY][tmpX])
            except IndexError:
                pass
            tmpX -=1 #because we keep subtracting we eventually run out of room for the list
            tmpY +=1
        if len(diagnolDownLeft) > 0:
            diagnolDownLeft.pop(0) #Get rid of the piece we started at
        if mode == 'get':
            keepGoing,spot = self.keepGoingMoves(diagnolDownLeft,'x',enemy)
            if keepGoing:
                possibleMoves.append([aY+(spot+1),aX-(spot+1)])
        else:
            keepGoing,spot = self.keepGoingMoves(diagnolDownLeft,acolor,enemy)
            if keepGoing:
                self.flip(aY,aX,aY+(spot),aX-(spot),acolor)
        #return this move set per PIECE
        if mode == 'get':
            return possibleMoves
#####################################################333
    def printBoard(self):
        count = 0
        rowcount = 0
        print("  X",end="")
        for i in range(8):
            print("  "+str(i),end = " ")
        print()
        print(" Y "+"+---"*8+"+")
        for row in self.board:
            print(" "+str(count)+" |",end="")
            for tile in row:
                if rowcount < 7:
                    print(" "+tile,end="  ")
                else:
                    print(" "+tile,end=" ")
                rowcount +=1            
            print("|")
            rowcount = 0
            count +=1
        print("   "+"+---"*8+"+"+"\n")

        
#####################################################333  
    def createTrainingMap(self,aBoard):
        parent = []
        for i in range(len(aBoard)):
            child = []
            for j in range(len(aBoard[i])):
                if self.board[i][j] == 'B':
                    child.append(1)
                elif self.board[i][j] == 'W':
                    child.append(-1)
                elif self.board[i][j] == 'x':
                    child.append(0)
            parent.append(child)
        return parent

    def isNotFull(self):
        for rows in self.board:
            for piece in rows:
                if piece == 'x':
                    return True
        return False

    def reset(self):
        for rows in range(len(self.board)):
            for piece in range(len(self.board[rows])):
                self.board[rows][piece]= 'x'
        self.board[3][3]='B'
        self.board[3][4]='W'
        self.board[4][4]='B'
        self.board[4][3]='W'
        self.gameHistory = []
    def cleanList(self,aList):
        newList = []
        for lists in aList:
            newList.append(lists)
        return newList
    
    def flip(self,startY,startX,flipY,flipX,acolor):
        print
        x = startX
        y = startY
        while x != flipX or y != flipY:
            self.board[y][x] = acolor
            if startX > flipX:
                x -=1
            if startX < flipX:
                x +=1
            if startY > flipY:
                y -=1
            if startY < flipY:
                y +=1
            self.board[y][x] = acolor
                 
                             
    def score(self):
        blackScore = 0
        for rows in self.board:
            for piece in rows:
                if piece == 'B':
                    blackScore +=1
        whiteScore = 64 - blackScore
        if blackScore > whiteScore:
            winner = "Black"
            winNum = 1
        elif blackScore < whiteScore:
            winner = "White"
            winNum = -1
        else:
            winner = "Tie"
            winNum = 0

        return blackScore, whiteScore, winner, winNum 

    def getOpenSpot(self,alist,piece):
        openS = 0
        try:
            openS = alist.index(piece)
        except ValueError:
            pass
        return openS
    
    def getOwnPiece(self,alist,spot,enemy):
        for i in alist[:spot]:
            if i != enemy:
                return False
        return True

    def keepGoingMoves(self,alist,token,enemy):
        spot = self.getOpenSpot(alist,token)
        keepGoing = self.getOwnPiece(alist,spot,enemy)
        if spot > 0 and keepGoing:
            return True, spot
        return False, 0
