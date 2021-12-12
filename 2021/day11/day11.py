"""
--- Day 11: Dumbo Octopus ---
https://adventofcode.com/2021/day/11

summary: track octopus flashes - recursive 2d grid tracking

Part 1: 1546
Part 2: 471
"""
from copy import deepcopy

def load_data():
    #datafile = 'input-day11-example'
    datafile = 'input-day11'
    data = []
    with open(datafile, 'r') as input:
        for line in input:
            data.append([int(x) for x in line.strip()])
    return data


def part1(pod):
    """
    There are 100 octopuses arranged neatly in a 10 by 10 grid
    Each octopus slowly gains energy over time and flashes brightly for a moment when its energy is full
    The energy level of each octopus is a value between 0 and 9

    You can model the energy levels and flashes of light in steps:
    - First, the energy level of each octopus increases by 1.
    - Then, any octopus with an energy level greater than 9 flashes.
      This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
      If this causes an octopus to have an energy level greater than 9, it also flashes.
      This process continues as long as new octopuses keep having their energy level increased beyond 9.
      (An octopus can only flash at most once per step.)
    - Finally, any octopus that flashed during this step has its energy level set to 0

    How many total flashes are there after 100 steps?
    """
    total_flashes = 0

    for step in range(100):
        # every octopus increases 1 energy level
        for y in range(10):
            for x in range(10):
                pod[y][x] += 1

        # any octopus with an energy level >9 flashes
        for y in range(10):
            for x in range(10):
                if pod[y][x] != "F" and pod[y][x] > 9:
                    pod, flashes = flash_octopus(x, y, pod, 0)
                    total_flashes += flashes

        # any octopus that flashed gets set to zero
        for y in range(10):
            for x in range(10):
                if pod[y][x] == "F":
                    pod[y][x] = 0

    return total_flashes


def flash_octopus(x, y, pod, flashes):
    flashes +=1 
    pod[y][x] = "F"

    directions = {
        "up": {
            "check_edge": y > 0,
            "y1": y-1,
            "x1": x,
        },
        "upleft": {
            "check_edge": y > 0 and x > 0,
            "y1": y-1,
            "x1": x-1,
        },
        "upright": {
            "check_edge": y > 0 and x < len(pod[0])-1,
            "y1": y-1,
            "x1": x+1,
        },
        "left": {
            "check_edge": x > 0,
            "y1": y,
            "x1": x-1,
        },
        "right": {
            "check_edge": x < len(pod[0])-1,
            "y1": y,
            "x1": x+1,
        },
        "down": {
            "check_edge": y < len(pod)-1,
            "y1": y+1,
            "x1": x,
        },
        "downleft": {
            "check_edge": y < len(pod)-1 and x > 0,
            "y1": y+1,
            "x1": x-1,
        },
        "downright": {
            "check_edge": y < len(pod)-1 and x < len(pod[0])-1,
            "y1": y+1,
            "x1": x+1,
        },
    }

    for dir in directions:
        x1 = directions[dir]["x1"]
        y1 = directions[dir]["y1"]
        if directions[dir]["check_edge"] and pod[y1][x1] != "F":
            pod[y1][x1] += 1
            if pod[y1][x1] > 9:
                pod, flashes = flash_octopus(x1, y1, pod, flashes)
    return pod, flashes


def part2(pod):
    """
    the flashes seem to be synchronizing!
    What is the first step during which all octopuses flash?
    """
    step = 0
    while True:
        step += 1

        # every octopus increases 1 energy level
        for y in range(10):
            for x in range(10):
                pod[y][x] += 1

        # any octopus with an energy level >9 flashes
        for y in range(10):
            for x in range(10):
                if pod[y][x] != "F" and pod[y][x] > 9:
                    pod, flashes = flash_octopus(x, y, pod, 0)
                    # when every octopus flashes, we're done
                    if flashes == 100:
                        return step

        # any octopus that flashed gets set to zero
        for y in range(10):
            for x in range(10):
                if pod[y][x] == "F":
                    pod[y][x] = 0


if __name__ == '__main__':
    data = load_data()
    print(f"Data1: {data}\n")
    print(f"Part 1: {part1(deepcopy(data))}\n")
    print(f"Part 2: {part2(deepcopy(data))}\n")
