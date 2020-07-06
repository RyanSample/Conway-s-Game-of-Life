from models.grid import Grid
from models.cell import Cell
from views.game import GameView
import sys
import copy
import time

NEIGHBORING_CELLS = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1) ,          (0, 1),
                    (1, -1) , (1, 0) , (1, 1)
                   ]

class Game():
    def __init__(self, grid_size, max_generation):
        self.grid_size = grid_size
        self.grid_size_x, self.grid_size_y = grid_size
        self.generation = 0
        self.max_generation = max_generation
        self.active_cells = 0
        self.game_board = Grid(grid_size, Cell)
        window_size = tuple([x * 5 for x in grid_size])
        self.view = GameView(window_size)
        self.empty_grid = Grid(self.grid_size, Cell)
        
    def run_game(self, frames_per_second = 100, display_after_end_of_game = True):
        """
        Begins running the game at an optional delay and persists the window unless display_after_end_of_game is False
        """
        keep_displaying_window = True         
        while (self.generation < self.max_generation) and keep_displaying_window:
            self.update_generation()
            keep_displaying_window = self.view.update_screen(self.generation)
            time.sleep(1/frames_per_second)
        
        while(keep_displaying_window and display_after_end_of_game):
            keep_displaying_window = self.view.update_screen(self.generation)

        sys.exit()

    def update_generation(self):
        """Checks each cell to see if it survives to the next generation"""
        next_generation = copy.deepcopy(self.empty_grid) # create new "dead" grid using deepcopy to avoid added iteration in the grid.__init__()

        self.view.redraw_screen() # reset screen

        row_number = 0
        for row in self.game_board:
            cell_number = 0
            for cell in row:
                number_neighbors = self.check_neighboring_living_cells((row_number, cell_number))
                if cell.is_living():
                    if number_neighbors == 2 or number_neighbors == 3:
                        next_generation.getGridItem(row_number, cell_number).toggle_living() # carry over living cell to next generation
                        self.view.draw_cell((row_number,cell_number)) # draw cell
                else:
                    if number_neighbors == 3:
                        next_generation.getGridItem(row_number, cell_number).toggle_living() # non-living cell becomes living in the next generation
                        self.view.draw_cell((row_number,cell_number)) # draw cell
                cell_number += 1
            row_number += 1
        
        self.game_board = next_generation #This generation has ended, copy next generation's grid into current grid
        self.generation += 1        

    def check_neighboring_living_cells(self, coordinates):
        """Check neighboring cells to see if they are living and return the number of living cells"""
        x, y = coordinates
        num_neighbors = 0
        for neighbor_coordinates in NEIGHBORING_CELLS:
            neighbor_x, neighbor_y = neighbor_coordinates
            neighbor_x = (neighbor_x + x) % self.grid_size_x
            neighbor_y = (neighbor_y + y) % self.grid_size_y
            if self.game_board.getGridItem(neighbor_x, neighbor_y).is_living():
                num_neighbors += 1

        return num_neighbors

    def load_coordinates_into_grid(self, coordinate_list):
        """Takes a list of coordinates, a tuple(int x, int y), and sets the corresponding cell to living
           Raises an IndexError if the coordinates are not
        """
        for coordinate in coordinate_list:
            x, y = coordinate
            if(x < self.grid_size_x and x >= 0 and y < self.grid_size_y and y >= 0):
                self.game_board.getGridItem(x, y).toggle_living()
            else:
                raise(IndexError)

    def get_game_board(self):
        """Returns the current generation's game board"""
        return self.game_board