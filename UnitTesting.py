'''
Created on 26-Nov-2019

@author: sneha
'''
import unittest
import Game
from Game import GridGame

class TestSum(unittest.TestCase):
    def test_create_grid_and_get_color_after_move(self):
        """
        Test that if the given function works without an error
        """
        N = 4
        M = 2
        b = GridGame(size=N, color=M) 
        moves, tileColorSequence = Game.getUserMovesAndColors(N, M, b);
        self.assertGreater(moves ,0, "is greater than zero in this case")
        self.assertIsNotNone(tileColorSequence,"is not None")



if __name__ == '__main__':
    unittest.main()
