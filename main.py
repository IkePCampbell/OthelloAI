from board import Board
from game import Game
from learn import Othello
import sys

if __name__ == "__main__":
    game = Game(Board())
    game.welcome()
    playersPlaying = game.selectPlayers()
    game.playOthello(playersPlaying)
    game.simulateManyGames(1000)

    


    