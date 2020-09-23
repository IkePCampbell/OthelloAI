from player import Player
from rando import Rando
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
        self.humanPlaying = True

    def welcome(self):
        print("\nWelcome to Othello\nTo make a move, please enter a desired coordinate in the form of (X,Y)\n")

    def selectPlayers(self):
        if self.humanPlaying != True:
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
                self.player1 = Player('Player1','B')
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
                self.gameBoard.printBoard()
                if self.humanPlaying == True:
                    print('Its',self.currentPlayer.playerName+"'s turn! ("+self.currentPlayer.tokenColor+")")
                moveList,canMove = self.gameBoard.canMove(self.currentPlayer.tokenColor)
                if canMove == False:
                    if self.humanPlaying == True:
                        print("There are no valid moves for you this turn")
                else:
                    # -- moveList is primarily for debugging, ensures the appropriate moves are available per turn based on pieces -- 
                    print(moveList)
                    invalid = True
                    while invalid:
                        # -- validation of input --
                        tokenYCoord, tokenXCoord =self.currentPlayer.getMove()
                        #-- index inside the nested lists -- 
                        testMove = [tokenXCoord, tokenYCoord]
                        if testMove in moveList:
                            invalid = False
                        # -- If there is a false move by the player, not the random agent --    
                        if self.currentPlayer.playerName != "Random":
                            print("Sorry, that is not a valid move!\n")
                    if self.currentPlayer.playerName == "Random":
                        if self.humanPlaying == True:
                            print("They place a piece at "+ str(tokenYCoord)+","+str(tokenXCoord))
                    self.gameBoard.moves(tokenYCoord,tokenXCoord,self.currentPlayer.tokenColor,'flip')
                    self.gameHistory.append(self.gameBoard.createTrainingMap(self.gameBoard))
                    #switch players
                if self.currentPlayerIndex == 0:
                    self.currentPlayerIndex = 1
                else:
                    self.currentPlayerIndex = 0
                self.currentPlayer = self.playerList[self.currentPlayerIndex] 
                playing = self.gameBoard.isNotFull()
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
            history = []
            for gameRound in self.gameHistory:
                history.append((winNum, gameRound))
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


    def simulateNeuralNetwork(self, nnPlayer, model):
        playerToMove = PLAYER_X_VAL
        while (self.getGameResult() == GAME_STATE_NOT_ENDED):
            availableMoves = self.getAvailableMoves()
            if playerToMove == nnPlayer:
                maxValue = 0
                bestMove = availableMoves[0]
                for availableMove in availableMoves:
                    # get a copy of a board
                    boardCopy = copy.deepcopy(self.board)
                    boardCopy[availableMove[0]][availableMove[1]] = nnPlayer
                    if nnPlayer == PLAYER_X_VAL:
                        value = model.predict(boardCopy, 0)
                    else:
                        value = model.predict(boardCopy, 2)
                    if value > maxValue:
                        maxValue = value
                        bestMove = availableMove
                selectedMove = bestMove
            else:
                selectedMove = availableMoves[random.randrange(0, len(availableMoves))]
            self.move(selectedMove, playerToMove)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL

    def getTrainingHistory(self):
        return self.trainingHistory

    def simulateManyGames(self, numberOfGames):
        b_wins = 0
        w_wins = 0
        ties = 0
        total = 0
        for i in range(numberOfGames):
            self.humanPlaying = False
            self.selectPlayers()
            result = self.playOthello()
            self.gameBoard.reset()
            if result == 1:
                b_wins += 1
            elif result == -1:
                w_wins+=1
            else:
                ties +=1 
            total +=1
            
        print ('B Wins: ' + str(int(b_wins * 100/total)) + '%')
        print('W Wins: ' + str(int(w_wins * 100 / total)) + '%')
        print('Draws: ' + str(int(ties * 100 / total)) + '%')


    def simulateManyNeuralNetworkGames(self, nnPlayer, numberOfGames, model):
        nnPlayerWins = 0
        randomPlayerWins = 0
        draws = 0
        print ("NN player")
        print (nnPlayer)
        for i in range(numberOfGames):
            self.resetBoard()
            self.simulateNeuralNetwork(nnPlayer, model)
            if self.getGameResult() == nnPlayer:
                nnPlayerWins = nnPlayerWins + 1
            elif self.getGameResult() == GAME_STATE_DRAW:
                draws = draws + 1
            else: randomPlayerWins = randomPlayerWins + 1
        totalWins = nnPlayerWins + randomPlayerWins + draws
        print ('X Wins: ' + str(int(nnPlayerWins * 100/totalWins)) + '%')
        print('O Wins: ' + str(int(randomPlayerWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')