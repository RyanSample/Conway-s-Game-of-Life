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