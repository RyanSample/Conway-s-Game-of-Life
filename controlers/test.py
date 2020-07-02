import unittest
from game import Game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.dimensions = 250, 250
        self.game = Game(dimensions)

    def testGame(self):
        pass
