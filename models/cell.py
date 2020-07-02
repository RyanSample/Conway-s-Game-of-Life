class Cell():
    def __init__(self, status = False):
        self.living = status
        self.number_neighbors = 0

    def is_living(self):
        return self.living

    def decrement_neighbors(self):
        self.number_neighbors += 1

    def increment_neigbors(self):
        self.number_neighbors -= 1

    def get_number_neighbors(self):
        return self.number_neighbors

    def toggle_living(self):
        self.living = not self.living

    def __str__(self):
        if self.living:
            return "X"
        return " "
