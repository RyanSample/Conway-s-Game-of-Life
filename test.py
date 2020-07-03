import unittest
#from models import test as models_test
#from views import test as views_test
from game import Game

CORNER_TEST_COORDINATES = [(0,0),(24,24),(0,24)]
FOUR_NEIGHBORS_TEST = [(0,0), (0,1), (1,1), (1,0), (4,4)] #(0,0) has 4 neighbors will disappear after 1 generation
ONE_NEIGHBOR_TEST = [(0,0), (0,1)] 
TWO_NEIGHBORS_TEST = [(0,0), (0,1), (1,0)]
THREE_NEIGHBORS_TEST = [(0,1), (1,1), (1,0)]

class GameControllerTestCase(unittest.TestCase):

    def test_corners(self):
        """Start a new controller and load corners into it. Verify that all four corner become alive after 1 generation"""
        game_controller = Game((25,25), 5)
        game_controller.load_coordinates_into_grid(CORNER_TEST_COORDINATES)
        game_controller.update_generation()
        self.assertEqual(game_controller.get_game_board().getGridItem(24,0).is_living(), True)

    def test_four_neighbors(self):
        """Test that a cell with 4 or more neighbors is no longer living in the next generation"""
        game_controller = Game((5,5), 5)
        game_controller.load_coordinates_into_grid(FOUR_NEIGHBORS_TEST)
        game_controller.update_generation()
        self.assertEqual(game_controller.get_game_board().getGridItem(0,0).is_living(), False)

    def test_one_neighbor(self):
        """Test that a cell with 1 neighbor is no longer living in the next generation"""
        game_controller = Game((5,5), 5)
        game_controller.load_coordinates_into_grid(ONE_NEIGHBOR_TEST)
        game_controller.update_generation()
        self.assertEqual(game_controller.get_game_board().getGridItem(0,0).is_living(), False)

    def test_two_neighbors(self):
        """Test that a cell with 2 neighbors is living in the next generation"""
        game_controller = Game((4,4), 5)
        game_controller.load_coordinates_into_grid(TWO_NEIGHBORS_TEST)
        game_controller.update_generation()
        self.assertEqual(game_controller.get_game_board().getGridItem(0,0).is_living(), True)

    def test_empty_cell_three_neighbors(self):
        """
           Tests that a non-living cell with three neighbors is alive in the subsequent generation 
           this test also checks that the cell is still living in the next generation
        """
        game_controller = Game((4,4), 5)
        game_controller.load_coordinates_into_grid(THREE_NEIGHBORS_TEST)
        game_controller.update_generation()
        self.assertEqual(game_controller.get_game_board().getGridItem(0,0).is_living(), True)
        game_controller.update_generation()
        self.assertEqual(game_controller.get_game_board().getGridItem(0,0).is_living(), True)

    def test_load_coordinates_out_of_game(self):
        game_controller = Game((4,4), 5)
        cl = [(5,5)]
        with self.assertRaises(IndexError):
            game_controller.load_coordinates_into_grid(cl)

def suite():
    suite = unittest.TestSuite()
    #suite.addTest(models_test.suite()) # Currently these test suites are not working because they appear to be executed in the wrong directory
    #suite.addTest(views_test.suite())  # so, the modules they require are not being imported into those test.
    suite.addTest(unittest.makeSuite(GameControllerTestCase, 'ControllerTest'))
    return suite
