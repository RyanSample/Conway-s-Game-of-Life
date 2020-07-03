import unittest

from grid import Grid
from cell import Cell 

class CellTestCase(unittest.TestCase):
    def setUp(self):
        """Create a default cell, a living cell, and a dead cell"""
        self.cell = Cell()
        self.livingCell = Cell(True)
        self.deadCell = Cell(False)

    def test_toggle_cell(self):
        """Test that the toggle living function works as anticipated by setting a cell to living then dead."""
        self.cell.toggle_living()
        self.assertEqual(self.cell.is_living(), True)
        self.cell.toggle_living()
        self.assertEqual(self.cell.is_living(), False)

    def test_print_cell(self):
        """Test that the a living cell prints out an X and a dead cell prints out a space
           Note - this print function is not used in the final implementation, it is used for testing
        """
        self.assertEqual(str(self.deadCell), " ")
        self.assertEqual(str(self.livingCell), "X")

class GameBoardTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a grid of 100 x 100 cells"""
        self.gameBoard = Grid((100, 100), Cell)

    def test_toggle_cell_in_board(self):
        """Verifies that the toggle living function is being called"""
        self.gameBoard.getGridItem(50, 50).toggle_living()
        self.assertEqual(self.gameBoard.getGridItem(50,50).is_living(), True)

    def test_gameboard_size(self):
        """Verifies that the functions returning the size of the grid return the correct value"""
        self.assertEqual(self.gameBoard.get_size(), (100, 100))
        self.assertEqual(self.gameBoard.get_columns(), 100)
        self.assertEqual(self.gameBoard.get_rows(), 100)

    def test_out_of_bounds_calls(self):
        """Test that verifies that an IndexError is raised when a call to get"""
        with self.assertRaises(IndexError):
            self.gameBoard.getGridItem(101,101)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GameBoardTestCase, 'GameBoardTest'))
    suite.addTest(unittest.makeSuite(CellTestCase, 'CellTest'))
    return suite

if __name__ == "__main__":
    unittest.main()