from player import Player
from rando import Rando
from smartOthello import Smart

import random
class Game():
    def __init__(self, board):
        self.gameBoard = board
        self.currentPlayer = None
        self.currentPlayerIndex = None
        self.playerList = []
        self.player1 = None
        self.player2 = None
        self.playAgain = True
        self.gameHistory = []
        self.playersPlaying = None
        self.randomPlayers = False
        self.humanPlaying = False
        self.othelloAgent= False
        self.noMoves = 0
        self.outPut = []
        self.nnHistory = []
    def welcome(self):
        print("\nWelcome to Othello\nTo make a move, please enter a desired coordinate in the form of (X,Y)\n")

    def selectPlayers(self,model,test):
        if self.othelloAgent == True and test == "B":
            self.player1 = Rando('Random','W')
            self.player2 = Smart('SmartOthello','B',model)

        elif self.othelloAgent == True and test == "W":
            self.player1 = Rando('Random','B')
            self.player2 = Smart('SmartOthello','W',model)
            self.playersPlaying = 3

        elif self.randomPlayers == True:
            self.player1 = Rando('Random','B')
            self.player2 = Rando('Random','W')
            self.playersPlaying = 3
        else: 
            players = input("How many players are playing, you can have 1 or 2?: ")
            while players.isdigit() == False or players not in ["1","2","3"]:
                print("Invalid input")
                players = input("How many players are playing, you can have 1 or 2?")  

            if int(players) == 1:
                self.player1 = Player('Player','B')
                self.player2 = Rando('Random','W')
                self.playersPlaying = 1
            if int(players) == 2:
                self.player1 = Player('Player1','W')
                self.player2 = Player('Player2','B')
                self.playersPlaying = 2

        self.playerList = [self.player1, self.player2]
        goesFirst = random.randint(0,1)
        if goesFirst == 0:
            if self.humanPlaying == True:
                print(self.player1.playerName+", you will go first; your color is White")
            start = 0
        else:
            if self.humanPlaying == True:
                print(self.player2.playerName+", you will go first; your color is Black")
            start = 1
        self.currentPlayer = self.playerList[start]
        self.currentPlayerIndex = start

    def playOthello(self):
        while self.playAgain == True:
            playing = True
            #Whoever wins the "coin" flip to start
            while(playing):
                if self.humanPlaying == True:
                    self.gameBoard.printBoard()  
                    print('Its',self.currentPlayer.playerName+"'s turn! ("+self.currentPlayer.tokenColor+")")
                moveList,canMove = self.gameBoard.canMove(self.currentPlayer.tokenColor)
                if canMove == False:
                    self.noMoves +=1
                    if self.humanPlaying == True:
                        print("There are no valid moves for you this turn")
                else:
                    # -- moveList is primarily for debugging, ensures the appropriate moves are available per turn based on pieces -- 
                    self.noMoves = 0
                    invalid = True
                    while invalid != False:
                        # -- validation of input --
                        tokenYCoord, tokenXCoord =self.currentPlayer.getMove(moveList)
                        #-- index inside the nested lists -- 
                        testMove = [tokenXCoord, tokenYCoord]
                        if testMove in moveList:
                            invalid = False
                        # -- If there is a false move by the player, not the random agent --    
                            if self.currentPlayer.playerName== "Player":
                                print("Sorry, that is not a valid move!\n")
                        if self.humanPlaying == True:
                            self.gameBoard.printBoard()
                            print("They place a piece at "+ str(tokenYCoord)+","+str(tokenXCoord))
                    self.gameBoard.moves(tokenYCoord,tokenXCoord,self.currentPlayer.tokenColor,'flip')
                    self.gameHistory.append(testMove)
                    #switch players
                if self.currentPlayerIndex == 0:
                    self.currentPlayerIndex = 1
                else:
                    self.currentPlayerIndex = 0
                self.currentPlayer = self.playerList[self.currentPlayerIndex] 
                playing = self.gameBoard.isNotFull(self.noMoves)
            if self.humanPlaying == True:
                self.gameBoard.printBoard()
                print("The Game is over!")
            blackScore, whiteScore, winner, winNum = self.gameBoard.score()
            if winner == "Tie":
                if self.humanPlaying == True:
                    print("There was no winner! It was a tie! Black scored 32, White Scored 32")
            else:
                if self.humanPlaying == True:
                    print(winner,"wins! Black scored",str(blackScore)+", White Scored",str(whiteScore))
            print()
            for gameRound in range(len(self.gameHistory)):
                result = ""
                for item in self.gameHistory[gameRound]:
                    result += str(item)
                self.nnHistory.append(list(map(int,result)))
                self.outPut.append(winNum)
            self.gameHistory = []
            #If there are 2 players we shouldnt prompt
            if self.playersPlaying == 1:
                goAgain = input("Would you like to play again? (Y)es or (N)o: ")
                while goAgain not in ["N","Y"]:
                    print("Sorry, I didn't recognize that.")
                    goAgain = input("Would you like to play again? (Y)es or (N)o: ")
                if goAgain == "N":
                    print("Exiting")
                    self.playAgain = False
                elif goAgain == "Y":
                    self.gameBoard.reset()
            else: #implement neural network check here
                return winNum

    def getTrainingHistory(self):
        return self.gameHistory

    def simulateManyGames(self, numberOfGames):
        b_wins = 0
        w_wins = 0
        ties = 0
        total = 0
        print("Playing",numberOfGames,"games....")
        for i in range(numberOfGames):
            self.randomPlayers = True
            self.selectPlayers(None,None)
            result = self.playOthello()
            print("Completed game", i+1)
            self.gameBoard.reset()
            if result == 1:
                b_wins += 1
            elif result == 2:
                w_wins+=1
            else:
                ties +=1 
            total +=1

        print("After playing",numberOfGames,"here are the results")
        print ('B Wins: ' + str(int(b_wins * 100/total)) + '%')
        print('W Wins: ' + str(int(w_wins * 100 / total)) + '%')
        print('Draws: ' + str(int(ties * 100 / total)) + '%')

    def simulateNNGames(self, numberOfGames,model,color):
        b_wins = 0
        w_wins = 0
        ties = 0
        total = 0
        print("Playing",numberOfGames,"games....")
        for i in range(numberOfGames):
            self.othelloAgent = True
            self.selectPlayers(model,color)
            result = self.playOthello()
            print("Completed game", i+1)
            self.gameBoard.reset()
            if result == 1:
                b_wins += 1
            elif result == 2:
                w_wins+=1
            else:
                ties +=1 
            total +=1

        if color == "B":
            print("After playing",numberOfGames,"(s) here are the results")
            print ('The Agent won: ' + str(int(b_wins * 100/total)) + '%')
            print('The Agent lost: ' + str(int(w_wins * 100 / total)) + '%')
            print('Draws: ' + str(int(ties * 100 / total)) + '%')
        else:
            print("After playing",numberOfGames,"(s) here are the results")
            print ('The Agent won:' + str(int(w_wins * 100/total)) + '%')
            print('The Agent lost: ' + str(int(b_wins * 100 / total)) + '%')
            print('Draws: ' + str(int(ties * 100 / total)) + '%')
