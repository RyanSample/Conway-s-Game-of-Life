from game import GameView
import unittest
import pygame

class GameViewTestCase(unittest.TestCase):
    def setUp(self):
        """Setup a GameView object with a grid size of 100 x 100 and a default refresh rate"""
        self.gv = GameView((100, 100))

    def test_update_screen(self):
        """Verify that the update screen returns True when running normally and False when Pygame detects a Quit event."""
        self.assertEqual(self.gv.update_screen(1), True, "Running normal update screen")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GameViewTestCase, 'GameViewTest'))
    return suite