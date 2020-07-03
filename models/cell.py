class Cell():
    def __init__(self, status = False):
        """"""
        self.living = status
        self.number_neighbors = 0

    def is_living(self):
        """Return a boolean value indicating whether the cell is living or not"""
        return self.living

    def decrement_neighbors(self):
        """Deprecated"""
        self.number_neighbors += 1

    def increment_neigbors(self):
        """Deprecated"""
        self.number_neighbors -= 1

    def get_number_neighbors(self):
        """Deprecated"""
        return self.number_neighbors

    def toggle_living(self):
        """Toggles the cells status as living"""
        self.living = not self.living

    def __str__(self):
        if self.living:
            return "X"
        return " "
