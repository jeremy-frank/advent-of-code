"""
day24ab - https://adventofcode.com/2020/day/24

--- Day 24: Lobby Layout ---

* Part 1
The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern
The tiles are all white on one side and black on the other.
They start with the white side facing up.
Each line in the list identifies a single tile that needs to be flipped by giving a 
  series of steps starting from a reference tile
Every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast.
  e, se, sw, w, nw, ne
Each time a tile is identified, it flips from white to black or from black to white.
Tiles might be flipped more than once.

esenee = start at the reference tile and then move one tile east, one tile southeast, 
         one tile northeast, and one tile east.

Example: 10 tiles are black

After all of the instructions have been followed, how many tiles are left with the black side up?
459

* Part 2
- Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
- Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

Tiles immediately adjacent means the six tiles directly touching the tile in question.
The rules are applied simultaneously to every tile.

Example: After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?
4150

Notes: Added clean_grid afterwards
- Before clean_grid: size of the final grid is 12011 tiles
- After clean_grid: size of the final grid is 10870 tiles

"""
import copy

def load_data():
    tiles = []
    #datafile = 'input-day24-example'
    datafile = 'input-day24'
    with open(datafile, 'r') as input:
        for line in input:
            tiles.append(chop(line.strip()))
    return tiles


def chop(line):
    instructions = []
    while line:
        if line.startswith("e"):
            instructions.append("e")
            line = line[1:]
        elif line.startswith("w"):
            instructions.append("w")
            line = line[1:]
        elif line.startswith("nw"):
            instructions.append("nw")
            line = line[2:]
        elif line.startswith("sw"):
            instructions.append("sw")
            line = line[2:]
        elif line.startswith("ne"):
            instructions.append("ne")
            line = line[2:]
        elif line.startswith("se"):
            instructions.append("se")
            line = line[2:]
    return instructions


def part1(tiles):
    grid = {}

    for tile in tiles:
        x, y = navigate(tile)

        if y not in grid:
            grid[y] = {}

        if x not in grid[y] or grid[y][x] == "w":
            grid[y][x] = "b"
        else:
            grid[y][x] = "w"
    
    black_tiles = 0
    for y in grid:
        for x in grid[y]:
            if grid[y][x] == "b":
                black_tiles += 1

    return black_tiles, grid


def navigate(directions):
    moves = {
        "e": (2, 0),
        "w": (-2, 0),
        "se": (1, -1),
        "ne": (1, 1),
        "sw": (-1, -1),
        "nw": (-1, 1),
    }

    x = 0
    y = 0
    for direction in directions:
        x += moves[direction][0]
        y += moves[direction][1]

    return x, y


def part2(grid):
    moves = {
        "e": (2, 0),
        "w": (-2, 0),
        "se": (1, -1),
        "ne": (1, 1),
        "sw": (-1, -1),
        "nw": (-1, 1),
    }

    day = 0
    while day < 100:
        day += 1
        grid = clean_grid(grid)
        grid = pad_grid(grid, moves)
        grid = process_grid(grid, moves)

    black_tiles = 0
    grid_size = 0
    for y in grid:
        for x in grid[y]:
            grid_size += 1
            if grid[y][x] == "b":
                black_tiles += 1
    print(f"Size of the final grid is {grid_size} tiles")
    return black_tiles    


def clean_grid(grid):
    """remove all the white tiles from the grid"""
    new_grid =copy.deepcopy(grid)

    for y in grid:
        for x in grid[y]:
            if grid[y][x] == "w":
                del new_grid[y][x]
                if new_grid[y] == {}:
                    del new_grid[y]
    return new_grid


def pad_grid(grid, moves):
    """pad the grid with a white tile in any blank spot next to a black tile"""
    new_grid =copy.deepcopy(grid)

    for y in grid:
        for x in grid[y]:
            if grid[y][x] == "b":
                for move in moves:
                    ymove = y + moves[move][1]
                    xmove = x + moves[move][0]
                    if ymove not in new_grid:
                        new_grid[ymove] = {}
                    if xmove not in new_grid[ymove]:
                        new_grid[ymove][xmove] = "w"

    return new_grid


def process_grid(grid, moves):
    """check every tile in the grid and flip it according to the rules"""
    new_grid ={}

    for y in grid:
        new_grid[y] = {}
        for x in grid[y]:
            side = check_adjacent(y, x, grid, moves)
            new_grid[y][x] = side
    return new_grid


def check_adjacent(y, x, grid, moves):
    black_adjacent = 0
    for move in moves:
        ymove = y + moves[move][1]
        xmove = x + moves[move][0]
        if ymove in grid:
            if xmove in grid[ymove]:
                if grid[ymove][xmove] == "b":
                    black_adjacent += 1

    center = grid[y][x]
    if center == "b":
        if black_adjacent == 0 or black_adjacent > 2:
            return "w"
        else:
            return "b"
    elif center == "w":
        if black_adjacent == 2:
            return "b"
        else:
            return "w"


if __name__ == '__main__':
    data = load_data()
    print("tiles:")
    for line in data:
        print(line)

    black_tiles, grid = part1(data)
    print(f"\nPart 1 - {black_tiles}")

    black_tiles = part2(grid)
    print(f"Part 2 - {black_tiles}")
