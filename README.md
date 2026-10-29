# Vehicle Rental Fleet Manager

A command-line program in Python to manage a small fleet of rental vehicles. It lets you register, search, update and save vehicles, and calculate fleet costs through a simple text menu.

This is a study project focused on functions, dictionaries, loops and file handling.

## Features

| Option | Description |
|--------|-------------|
| 1 | Register a vehicle (year, license plate, model, daily rental price) |
| 2 | Look up a vehicle by license plate |
| 3 | Show the total daily price of the whole fleet |
| 4 | Show the newest vehicle whose daily rental is below a given value |
| 5 | Exit |
| 6 | Save the fleet to a file (`veiculos.txt`) |
| 7 | Load the fleet from the file |
| 8 | Update a vehicle (press Enter to keep the current value) |

The fleet is limited to 5 vehicles (`NUM_VEICULOS`).

## Concepts practiced

Dictionaries to represent each vehicle
Functions with type hints (list[dict], -> float, -> int)
while loop for the main menu and for loops with enumerate
Conditionals (if) to handle each menu option
Reading and writing text files with pathlib.Path
String handling (strip, upper, split) and f-string formatting
Optional values with dict.get()


## How it works

Each vehicle is stored as a dictionary:

python
{
    "ano": 1998,
    "placa": "AAA-8888",
    "modelo": "Gol",
    "aluguelDia": 89.9
}

When saved, the fleet is written to veiculos.txt, one vehicle per line, with fields separated by semicolons:

1998;AAA-8888;Gol;89.9

Author

Gustavo Fraga Apellaniz GitHub: @GustavoApellaniz
