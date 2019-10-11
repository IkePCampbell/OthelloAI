from board import Board
from player import Player
from rando import Rando
import random
import sys

gameBoard = Board()

print()
print("Welcome to Othello")
print("To make a move, please enter a desired coordinate in the form of (X,Y)")
print()

players = input("How many players are playing, you can have 1 or 2?: ")
while players.isdigit() == False or players not in ["1","2"]:
    print("Invalid input")
    players = input("How many players are playing, you can have 1 or 2?")

if int(players) == 1:
    player1 = Player('Player','B')
    player2 = Rando('Random','W')
else:
    player1 = Player('Player1','B')
    player2 = Player('Player','W')

playerList = [player1,player2]

playAgain = True
while playAgain == True:
    goesFirst = random.randint(0,1)
    if goesFirst == 0:
        print(player1.playerName+", you will go first; your color is White")
        start = 0
    else:
        print(player2.playerName+", you will go first; your color is Black")
        start = 1
    playing = True
    #Whoever wins the "coin" flip to start
    currentPlayer = playerList[start]
    currentPlayerIndex = start
    while(playing):
        gameBoard.printBoard()
        print('Its',currentPlayer.playerName+"'s turn! ("+currentPlayer.tokenColor+")")
        moveList,canMove = gameBoard.canMove(currentPlayer.tokenColor)
        if canMove == False:
            print("There are no valid moves for you this turn")
        else:
            #print(moveList)
            invalid = True
            while invalid:
                # -- validation of input --
                tokenXCoord, tokenYCoord =currentPlayer.getMove()
                #-- index inside the nested lists -- 
                testMove = [tokenXCoord, tokenYCoord]
                if testMove in moveList:
                    invalid = False
            if currentPlayer.playerName == "Random":
                print("They place a piece at "+ str(tokenXCoord),str(tokenYCoord))
            gameBoard.moves(tokenYCoord,tokenXCoord,currentPlayer.tokenColor,'flip')
            
            #switch players
        if currentPlayerIndex == 0:
            currentPlayerIndex = 1
        else:
            currentPlayerIndex = 0
        currentPlayer = playerList[currentPlayerIndex] 
        playing = gameBoard.isNotFull()
    gameBoard.printBoard()
    print("The Game is over!")
    blackScore, whiteScore, winner = gameBoard.score()
    if winner == "Tie":
        print("There was no winner! It was a tie! Black scored 32, White Scored 32")
    else:
        print(winner,"wins! Black scored",str(blackScore)+", White Scored",str(whiteScore))
    print()
    goAgain = input("Would you like to play again? (Y)es or (N)o: ")
    while goAgain not in ["N","Y"]:
        print("Sorry, I didn't recognize that.")
        goAgain = input("Would you like to play again? (Y)es or (N)o: ")
    if goAgain == "N":
        print("Exiting")
        playAgain = False
    elif goAgain == "Y":
        gameBoard.reset()


    


    