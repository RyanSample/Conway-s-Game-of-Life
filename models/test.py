import unittest

from grid import Grid
from cell import Cell 

class CellTestCase(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()
        self.livingCell = Cell(True)
        self.deadCell = Cell(False)

    def test_toggle_cell(self):
        self.cell.toggle_living()
        self.assertEqual(self.cell.is_living(), True)
        self.cell.toggle_living()
        self.assertEqual(self.cell.is_living(), False)

    def test_print_cell(self):
        self.assertEqual(str(self.deadCell), " ")
        self.assertEqual(str(self.livingCell), "X")

class GameBoardTestCase(unittest.TestCase):
    def setUp(self):
        self.gameBoard = Grid((100, 100), Cell)

    def test_toggle_cell_in_board(self):
        self.gameBoard.getGridItem(50, 50).toggle_living()
        self.assertEqual(self.gameBoard.getGridItem(50,50).is_living(), True)

if __name__ == "__main__":
    unittest.main()