from board import Board
from game import Game
from learn import Othello
import numpy as np
import decimal

if __name__ == "__main__":
    train_game = Game(Board())
    train_game.welcome()
    #tain_game.selectPlayers(None,None)
    #train_game.playOthello()
    #train_game.simulateManyGames(10)
    #train_game.simulateManyGames(100)
    #train_game.simulateManyGames(1000)
    train_game.simulateManyGames(10000) 
    train_in = np.array(train_game.nnHistory)
    train_out = np.array([train_game.outPut]).T
    OthelloModel = Othello(len(train_out))
    print("Random Generated Weights")
    print(OthelloModel.synaptic_weights)
    print("Training")
    OthelloModel.train(train_in,train_out,15000)
    print("Weights after training")
    print(OthelloModel.synaptic_weights)
    print("\n Model is Ready! \n")

    print("Testing Black Wins")
    train_game.simulateNNGames(1000,OthelloModel,"B")
    print("Testing White Wins")
    train_game.simulateNNGames(1000,OthelloModel,"W")