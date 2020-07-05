# Conway's Game of Life

A Python implementation of Conway's Game of Life built to be simple without sacrificing readablity.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See Installation for information on installing the program.

### Prerequisites
Conway's game of life requires Python 3.7 or greater.

To install the dependencies required to run this program, navigate to the project's root directory and simply type:

```
pip install -r requirements.txt 
```

### Installation

*This is a work in progress, currently there are issues installing this application due to an issue with pygame's dependencies*

To install run the following command to install requests

```
py -m pip install requests
```

Then run the installation script

```
py setup.py install
```

*At this point the installation may fail as follows*

```
error: The 'pygame==1.9.6' distribution was not found and is required by Game-Of-Life
```

## Running the program

To run the program you can simply type 
```
py main.py
```

This will run the following main function 
```
def main():
    gm = Game(game_size, 10000)
    gm.load_coordinates_into_grid(infinite_growth_pattern)
    gm.run_game(20)
```

1. This starts out by initializing a Game object which is passed a game size *tuple(int:size_x_axis, int:size_y_axis)* and the max number of generations, an int that will stop the game when that generation is reached. 
    1. **WARNING** The larger you make the game, the slower it will run, because each cell will need to be checked each generation.

1. The `Game.load_coordinates_into_grid()` function takes a list of coordinates and loads them into the Game's grid object. The coordinates are a tuple(int:x, int:y). Several other coordinate dictionaries representing different patterns are included in the main.py module and they can be passed to this function or you can create your own coordinate dictionaries and load them into the game!

1. Finally the `gm.run_game(int:frames_per_second)` function is responsible for running the game which will launch a window
initializing a Game object and run the game until the window is closed or the last generation is displayed

## Running the tests

Run tests by navigating to their directory and running the following command:

```
py -m unittest
```

## Built With

* [PyGame](https://www.pygame.org/) - The library used to display the Game of Life

## Authors

* **Ryan Sample** - [RyanSample](https://github.com/RyanSample)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* In memory of [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) 26 December 1937 – 11 April 2020