from board import Board
from game import Game
from learn import Othello

if __name__ == "__main__":
    game = Game(Board())
    game.welcome()
    #game.selectPlayers()
    #game.playOthello()
    game.simulateManyGames(100)