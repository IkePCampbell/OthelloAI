class Board:
    def __init__(self):
        self.full = False
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
        enemy = ''
        if acolor == "W":
            enemy = "B"
        else:
            enemy = "W"
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
        #need to find if the piece to its left is the opposite color 
        #move all around 
        #print("Starting Positions",aX,aY,acolor)
##################################################################################
        leftOf = self.board[aY][:aX]
        leftOf.reverse()
        goLeft = 0
        try:
            goLeft = leftOf.index('x')
            ownPieceLeft = leftOf.index(acolor)
        except ValueError:
            pass
        if goLeft > 0:
            if mode == 'get':
                possibleMoves.append([aY,aX-(goLeft+1)])
            else:
                self.flip(aY,aX,aY,aX-(goLeft),acolor)
   
        rightOf = self.board[aY][aX+1:] #have to add 1 to not include the original
        goRight = 0
        if len(rightOf) > 0:
            rightOf.pop()
        try:
            goRight = rightOf.index('x')
        except ValueError:
            pass
        if goRight > 0: 
            if mode == 'get':
                possibleMoves.append([aY,aX+(goRight+1)])
            else:
                self.flip(aY,aX,aY,aX+(goRight),acolor)
        
        aboveOf = []
        for i in range(0,aY): #get all possible spots above you
            aboveOf.append(self.board[i][aX])
        aboveOf.reverse()
        goUp = 0
        try:
            goUp = aboveOf.index('x')
        except ValueError:
            pass
        if goUp > 0:
            if mode == 'get':
                possibleMoves.append([aY-(goUp+1),aX])
            else:
                self.flip(aY,aX,aY-(goUp),aX,acolor) 
##################################################################################
        belowOf = []
        for i in range(aY+1,len(self.board)): #get all possible spots above you
            belowOf.append(self.board[i][aX])
        goDown = 0
        try:
            goDown = belowOf.index('x')
        except ValueError:
            pass
        if goDown > 0:
            if mode == 'get':
                possibleMoves.append([aY+(goDown+1),aX]) 
            else:
                self.flip(aY,aX,aY+(goDown),aX,acolor)
#####################################################333
        diagnolUpRight = []
        tmpX = aX
        for i in range(aY,-1,-1): #get all possible spots above you
            diagnolUpRight.append(self.board[i][tmpX])
            tmpX= (tmpX+1)% 8 #because we keep subtracting we eventually run out of room for the list
        if len(diagnolUpRight) > 0:
            diagnolUpRight.pop(0) #Get rid of the piece we started at
        goUDRight = 0
        try:
            goUDRight = diagnolUpRight.index('x')
        except ValueError:
            pass
        if goUDRight > 0: 
            if mode == 'get':
                possibleMoves.append([aY-(goUDRight+1),aX+(goUDRight+1)])
            else:
                self.flip(aY,aX,aY-(goUDRight),aX+(goUDRight),acolor)
#####################################################333
        diagnolUpLeft = []
        tmpX = aX
        for i in range(aY,-1,-1): #get all possible spots above you
            diagnolUpLeft.append(self.board[i][tmpX])
            tmpX= (tmpX-1)% 8 #because we keep subtracting we eventually run out of room for the list
        if len(diagnolUpLeft) > 0:
            diagnolUpLeft.pop(0) #Get rid of the piece we started at
        goUDLeft = 0
        testUDLeft = True
        try:
            goUDLeft = diagnolUpLeft.index('x')
        except ValueError:
            pass
        if goUDLeft > 0:
            if  mode == 'get':
                possibleMoves.append([aY-(goUDLeft+1),aX-(goUDLeft+1)])
            else:
                self.flip(aY,aX,aY-(goUDLeft),aX-(goUDLeft),acolor)
            #print(possibleMoves)
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
        #if len(diagnolDownRight) > 0:
         #   diagnolDownRight.pop(0) #Get rid of the piece we started at
        diagnolDownRight.reverse()
        if len(diagnolDownRight) > 0:
            diagnolDownRight.pop(0) #Get rid of the piece we started at
        goDDRight = 0
        try:
            goDDRight = diagnolDownRight.index('x')
        except ValueError:
            pass
        if goDDRight > 0:
            if (acolor not in diagnolDownRight):
                possibleMoves.append([aY+(goDDRight+1),aX+(goDDRight+1)]) 
            else:
                self.flip(aY,aX,aY+(goDDRight),aX+(goDDRight),acolor)
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
        goDDLeft = 0
        try:
            goDDLeft = diagnolDownLeft.index('x')
        except ValueError:
            pass
        if goDDLeft > 0:
            if (acolor not in diagnolDownLeft):
                possibleMoves.append([aY+(goDDLeft+1),aX-(goDDLeft+1)])
            else:
                self.flip(aY,aX,aY+(goDDLeft),aX-(goDDLeft),acolor)
        #return this move set per PIECE
        if mode == 'get':
            return possibleMoves

#####################################################333
    def printBoard(self):
        for row in self.board:
            for tile in row:
                print(tile, end = "  ")
            print()
#####################################################333  
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

    def cleanList(self,aList):
        newList = []
        for lists in aList:
            newList.append(lists)
        return newList
    
    def flip(self,startY,startX,flipY,flipX,acolor):
        x = startX
        y = startY
        while x != flipX or y != flipY:
            self.board[y][x] = acolor
            if startX > flipX:
                x -=1
            elif startX < flipX:
                x +=1
            if startY > flipY:
                y -=1
            elif startY < flipY:
                y +=1
                    
    def score(self):
        blackScore = 0
        for rows in self.board:
            for piece in rows:
                if piece == 'B':
                    blackScore +=1
        whiteScore = 64 - blackScore
        if blackScore > whiteScore:
            winner = "Black"
        elif blackScore < whiteScore:
            winner = "White"
        else:
            winner = "Tie"

        return blackScore, whiteScore, winner

