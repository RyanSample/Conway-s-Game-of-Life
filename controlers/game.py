from models.grid import Grid

neighboring_cells = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1) ,          (0, 1),
                    (1, -1) , (1, 0) , (1, 1)
                   ]

class Game():
    def __init__(self, grid_size):
        self.grid_size_x, self.grid_size_y = grid_size
        self.generation = 0
        self.active_cells = 0
        self.game_board = Grid(grid_size)

    def update_generation(self):
        next_generation = Grid(self.grid_size_x, self.grid_size_y) # create new "dead" grid and copy over living cells
        row_number = 0
        for row in self.game_board:
            cell_number = 0
            for cell in row:
                number_neighbors = self.check_neighboring_living_cells((row_number, cell_number)) # ToDo: remove the cell parameter
                if cell.is_living():
                    if number_neighbors == 2 or number_neighbors == 3:
                        next_generation.getGridItem(row_number, cell_number).toggle_living() # carry over living cell to next generation
                else:
                    if number_neighbors == 3:
                        next_generation.getGridItem(row_number, cell_number).toggle_living() # non-living cell becomes living in the next generation
                cell_number += 1
            row_number += 1
        
        self.game_board = next_generation #This generation has ended, copy next generation's grid into current grid
        self.generation += 1

    def check_neighboring_living_cells(self, coordinates):
        x, y = coordinates
        num_neighbors = 0
        for neighbor_coordinates in neighboring_cells:
            neighbor_x, neighbor_y = neighbor_coordinates
            neighbor_x = (neighbor_x + x) % self.grid_size_x
            neighbor_y = (neighbor_y + y) % self.grid_size_y
            if self.game_board.getGridItem(neighbor_x, neighbor_y).is_living():
                num_neighbors += 1

        return num_neighbors
