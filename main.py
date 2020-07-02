from models.grid import Grid
from models.cell import Cell
from views.game import GameView

from game import Game

import sys
game_size = 85, 45
window_size = tuple([5*x for x in game_size])

glider_coordinates = [
    (247,0),
    (245,1),
    (247,1),
    (246,2),
    (247,2)
]

toad = [
    (5, 5),
    (5, 6),
    (5, 7),
    (6, 6),
    (6, 7),
    (6, 8)
]

glider_gun = [
    (0,4), (1,4), (0,5), (1,5),
    (10,4), (10,5), (10,6), (11,3),
    (11,7), (12,2), (12,8), (13,2),
    (13,8), (14,5), (15,3), (15,7),
    (16,4), (16,5), (16,6), (17,5),
    (20,2), (20,3), (20,4), (21,2),
    (21,3), (21,4), (22,1), (22,5),
    (24,0), (24,1), (24,5), (24,6),
    (34,2), (34,3), (35,2), (35,3)

]

def main():
    #game = Game(game_size)
    pass
    #columns = 3
    #rows = 3
    #test_grid = Grid(rows , columns)
    #print(test_grid.__str__())
    #test_grid.getGridItem(2,2).toggle_living()
    #print(test_grid.__str__())

def test_view():
    rows, columns = game_size
    gv = GameView(window_size)
    grid = Grid(rows, columns)
    grid.getGridItem(213, 144).toggle_living()
    grid.getGridItem(2,2).toggle_living()

    while 1:
        gv.update_screen(grid)

def test_game():
    gm = Game(game_size, 1000)
    gm.load_coordinates_into_grid(glider_gun)
    gm.run_game(20)

def test_carriage_return():
    lst_of_strings = ["TEST1", "TEST2", "TEST3"]
    for line in lst_of_strings:
        print(line, end='\r')
    #print(lst_of_strings, end='\r')
    print("")

if __name__ == "__main__":
    #main()
    #test_carriage_return()
    #test_view()
    test_game()