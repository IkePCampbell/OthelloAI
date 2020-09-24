from board import Board
import unittest

class TestBoardMethods(unittest.TestCase):        
    def testLeft(self):
        #self.assertEqual(self.testBoard.canMove("B"))
        pass
#if __name__ == '__main__':
 #   unittest.main()

board = Board()
board.printBoard()
print(board.canMove("B"))
board.printBoard()
#print(board.canMove("B"))