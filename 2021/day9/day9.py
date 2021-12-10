"""
--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9

summary: recursive 2d grid exploration

Part 1: 491
Part 2: 1075536
"""
from copy import deepcopy

def load_data():
    #datafile = 'input-day9-example'
    datafile = 'input-day9'
    data = []
    with open(datafile, 'r') as input:
        for line in input:
            data.append([int(char) for char in line.strip()])
    return data


def part1(grid):
    """
    Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be
    Low points are the locations that are lower than any of its adjacent locations
    The risk level of a low point is 1 plus its height

    Find all of the low points on your heightmap.
    What is the sum of the risk levels of all low points on your heightmap?
    """
    low_points=[]
    for y_pos, line in enumerate(grid):
        for x_pos, point in enumerate(line):
            if check_for_low_point(grid, y_pos, x_pos, point):
                low_points.append(int(point))

    print(f"Low points: {low_points}")
    risk_level = sum(low_points) + len(low_points)
    return risk_level


def check_for_low_point(grid, y, x, point):
    # look up
    if y > 0 and point >= grid[y-1][x]:
        return False

    # look down
    if y < len(grid)-1 and point >= grid[y+1][x]:
        return False

    # look left
    if x > 0 and point >= grid[y][x-1]:
        return False

    # look right
    if x < len(grid[y])-1 and point >= grid[y][x+1]:
        return False

    return True


def part2(grid):
    """
    A basin is all locations that eventually flow downward to a single low point.
    Therefore, every low point has a basin
    Locations of height 9 do not count as being in any basin
    All other locations will always be part of exactly one basin.
    The size of a basin is the number of locations within the basin, including the low point. The example above has four basins

    What do you get if you multiply together the sizes of the three largest basins?
    """
    low_points=[]
    for y, line in enumerate(grid):
        for x, point in enumerate(line):
            if check_for_low_point(grid, y, x, point):
                low_points.append([y, x, int(point)])

    print(f"Low points: {low_points}")

    basins = []
    for low_point in low_points:
        print(f"\nFinding basin size for low point {low_point}")
        basin_size = find_basin_size(grid, low_point[0], low_point[1], low_point[2], 0)
        basins.append(basin_size)

    basins.sort()
    print(f"\nBasins: {basins}\n")
    basin_score = basins[-3] * basins[-2] * basins[-1]
    return basin_score


def find_basin_size(grid, y, x, point, size):
    """
    Recursively explore outward from the low point to find the size of the basin
    """
    grid[y][x] = "x"
    size += 1
    print(f"  point x{x} y{y} {point}, basin size {size}")

    # look up
    if y > 0 and grid[y-1][x] not in [9, "x"] and point < grid[y-1][x]:
        new_point = grid[y-1][x]
        size = find_basin_size(grid, y-1, x, new_point, size)

    # look down
    if y < len(grid)-1 and grid[y+1][x] not in [9, "x"] and point < grid[y+1][x]:
        new_point = grid[y+1][x]
        size = find_basin_size(grid, y+1, x, new_point, size)

    # look left
    if x > 0 and grid[y][x-1] not in [9, "x"] and point < grid[y][x-1]:
        new_point = grid[y][x-1]
        size = find_basin_size(grid, y, x-1, new_point, size)

    # look right
    if x < len(grid[0])-1 and grid[y][x+1] not in [9, "x"] and point < grid[y][x+1]:
        new_point = grid[y][x+1]
        size = find_basin_size(grid, y, x+1, new_point, size)

    return size


if __name__ == '__main__':
    data = load_data()
    print(f"Data1: {data}\n")
    print(f"Part 1: {part1(deepcopy(data))}\n")
    print(f"Part 2: {part2(deepcopy(data))}\n")
