from board import Board
from player import Player
import random

gameBoard = Board()
player1 = Player('player1','W')
player2 = Player('player2','B')
playerList = [player1,player2]

print()
print("Welcome to Othello player")
print("To make a move, please enter a desired coordinate in the form of (X,Y)")
print("To see the rules at anytime, please type 'rules' and you will be directed to the rules page")
print()
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
    invalid = True
    print(moveList)
    while invalid:
        # -- validation of input --
        tokenXCoord, tokenYCoord =currentPlayer.getMove()
        #index inside the nested lists
        testMove = [tokenXCoord, tokenYCoord]
        if testMove in moveList:
            invalid = False
    gameBoard.moves(tokenYCoord,tokenXCoord,currentPlayer.tokenColor,'flip')
    #switch players
    if currentPlayerIndex == 0:
        currentPlayerIndex = 1
    else:
        currentPlayerIndex = 0
    currentPlayer = playerList[currentPlayerIndex] 
    playing = gameBoard.isNotFull()
print("The Game is over!")
blackScore, whiteScore, winner = gameBoard.score()
if winner == "Tie":
    print("There was no winner! It was a tie! Black scored 32, White Scored 32")
else:
    print(winner,"wins! Black scored",str(blackScore)+", White Scored",str(whiteScore))

    


    