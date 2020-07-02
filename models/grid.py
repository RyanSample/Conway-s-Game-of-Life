
class Grid(object):
    def __init__(self, grid_size, object):
        """Creates a new grid with the supplied grid_size tuple(rows, columns) and instantiates a new object in each grid space"""
        self.rows, self.columns = grid_size
        self.grid = []
        for i in range(self.rows):
            self.grid.append([object() for j in range(self.columns)])

    def setGridItem(self, row, column, value):
        self.grid[row][column] = value

    def getGridItem(self, row, column):
        """Returns the grid item for a given row and column.
        
           Raises an index error if the row or column is out of bounds"""
        if row < self.rows and column < self.columns:
            return self.grid[row][column]
        else:
            raise(IndexError)

    def get_columns(self):
        """Returns the number of columns in the grid"""
        return self.columns

    def get_rows(self):
        """Returns the number of rows in the grid"""
        return self.rows

    def get_size(self):
        """Returns the total size of the grid as a tuple"""
        return self.rows, self.columns

    def __getitem__ (self, index):
        """Returns the item at index"""
        return self.grid[index]

    def __str__(self):
        """Converts grid object to a string"""
        string = ""
        for row in range(self.rows):
            for column in range(self.columns):
                string += str(self.grid[row][column])
            string += '\n'

        return string