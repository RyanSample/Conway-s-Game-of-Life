import pygame

CELL_WIDTH = 5

class GameView():
    def __init__(self, grid_size, refresh_rate = 1000):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 16)
        self.refresh_rate = refresh_rate
        self.grid_size = grid_size
        self.information_area = grid_size[0], 20
        self.window_size = (grid_size[0], grid_size[1] + self.information_area[1])
        self.screen = pygame.display.set_mode(self.window_size)
        self.cell_color = 0, 255, 0
        self.background_color = 0, 0, 0
        self.information_background_color = 0, 0, 255
        self.cell_size = 5, 5

    def update_text(self, text):
        """Writes the provided information to the lower area of the screen"""
        text_surface = self.font.render(str(text), False, (255,255,255))
        self.screen.blit(text_surface, (2, self.grid_size[1] + 2))

    def draw_cell(self, coordinates):
        """Given a tuple(int x, int y) draws a rectangle in the location offset by cell size"""
        x, y = coordinates
        rect = pygame.Rect(x*CELL_WIDTH, y*CELL_WIDTH, CELL_WIDTH, CELL_WIDTH)
        pygame.draw.rect(self.screen, self.cell_color, rect, 0)

    def redraw_screen(self):
        """Fills the screen with the set background color"""
        self.screen.fill(self.background_color)

    def update_screen(self, generation):
        """Checks for events and updates the screen at the end of each generation"""

        for event in pygame.event.get(): # if an event in pygame close the window
            if event.type == pygame.QUIT:
                return False

        self.update_text(generation)
        
        pygame.display.update() # update the display
        return True
