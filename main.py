from board import Board
from game import Game
from learn import Othello
import numpy as np

if __name__ == "__main__":
    game = Game(Board())
    game.welcome()
    #game.selectPlayers()
    #game.playOthello()
    game.simulateManyGames(5)
    #game.simulateManyGames(100)
    #game.simulateManyGames(1000)
    #game.simulateManyGames(10000) 
    train_in = np.array(game.nnHistory)
    train_out = np.array(game.outPut).T
    OthelloModel = Othello(len(train_out))
    print("Random Generated Weights")
    print(OthelloModel.synaptic_weights)
    print("Training")
    OthelloModel.train(train_in,train_out,500)
    print("Weights after training")
    print(OthelloModel.synaptic_weights)

    newsituation = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    print(OthelloModel.think(newsituation))