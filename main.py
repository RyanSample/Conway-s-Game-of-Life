from game import Game

import sys
game_size = 75, 75

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

infinite_growth_pattern = [
    (20,25), (22,24), (22,25), (24,21),
    (24,22), (24,23), (26,20), (26,21),
    (26,22), (27,21)
]

def main():
    gm = Game(game_size, 10000)
    gm.load_coordinates_into_grid(infinite_growth_pattern)
    gm.run_game(20)

if __name__ == "__main__":
    main()