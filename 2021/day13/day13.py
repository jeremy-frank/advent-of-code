"""
--- Day 13: Transparent Origami ---
https://adventofcode.com/2021/day/13

summary: fold a piece of transparent paper, see ASCII leters

Part 1: 675
Part 2: HZKHFEJZ

So, Part 2 printed out mirrored:
 #### ##   #### #### #  # #  # #### #  #
 #    #       #    # #  #  # # #    #  #
  #   #     ###  ### ####   ##  #   ####
   #  #       #    # #  #  # #   #  #  #
    # #  #    #    # #  #  # #    # #  #
 ####  ##  ####    # #  # #  # #### #  #

"""
from copy import deepcopy
from pprint import pprint


def load_data():
    # datafile = 'input-day13-example'
    datafile = "input-day13"
    points = []
    folds = []
    with open(datafile, "r") as input:
        for line in input:
            if "," in line:
                coords = line.strip().split(",")
                points.append([int(coord) for coord in coords])
            elif "fold" in line:
                foo = line.strip().split()
                bar = foo[2].split("=")
                folds.append([bar[0], int(bar[1])])

    return points, folds


def part1(points, folds):
    """
    Let's fold a piece of transparent paper
    0,0 represents the top-left coordinate
    The first value, x, increases to the right.
    The second value, y, increases downward

    There is a list of fold instructions
      fold the paper up (for horizontal y=... lines)
      fold the paper left (for vertical x=... lines)

    Some of the dots might end up overlapping after the fold is complete
    Dots will never appear exactly on a fold line
    Overlapping dots - in this case, the dots merge together and become a single dot

    How many dots are visible after completing just the first fold instruction on your transparent paper?
    """
    # find the biggest x and y values
    bigx, bigy = 0, 0
    for coords in points:
        x = coords[0]
        y = coords[1]
        if x > bigx:
            bigx = x
        if y > bigy:
            bigy = y

    # generate the empty grid
    grid = {}
    for iy in range(bigy + 1):
        grid[iy] = [" " for ix in range(bigx + 1)]

    # draw the points on the grid
    for coords in points:
        x = coords[0]
        y = coords[1]
        grid[y][x] = "#"

    # perform only the first fold
    fold = folds[0]
    fold_axis = fold[0]
    fold_line = fold[1]

    if fold_axis == "y":
        grid = fold_up_along_y(grid, fold_line)
    elif fold_axis == "x":
        grid = fold_left_along_x(grid, fold_line)

    # count the number of dots
    total_dots = 0
    for line in grid:
        for point in grid[line]:
            if point == "#":
                total_dots += 1

    return total_dots


def fold_up_along_y(grid, fold_line):
    # create new, smaller grid
    new_grid = {}
    for iy in range(fold_line):
        new_grid[iy] = [" " for ix in range(len(grid[0]))]

    # populate new grid
    for y in grid:
        for x, point in enumerate(grid[y]):
            if point == "#":
                # everything above the line gets copied (no change)
                if y < fold_line:
                    new_grid[y][x] = "#"
                # everything below the line gets flipped
                else:
                    adjusted_y = (fold_line - 1) - ((y - fold_line) - 1)
                    new_grid[adjusted_y][x] = "#"

    # print(f"\nGrid after y fold along {fold_line}:")
    # pprint(new_grid)
    return new_grid


def fold_left_along_x(grid, fold_line):
    # create new, smaller grid
    new_grid = {}
    new_x = len(grid[0]) - fold_line
    for iy in range(len(grid)):
        new_grid[iy] = [" " for ix in range(new_x)]

    # populate new grid
    for y in grid:
        for x, point in enumerate(grid[y]):
            if point == "#":
                # everything to the right of the line gets shifted to the left
                if x > fold_line:
                    new_grid[y][x - fold_line - 1] = "#"
                # everything to the left of the line gets flipped
                else:
                    # 1 2 3 4 5 6 7 8 9
                    #         F 0 1 2 3
                    adjusted_x = fold_line - 1 - x
                    new_grid[y][adjusted_x] = "#"

    # print(f"\nGrid after x fold along {fold_line}:")
    # pprint(new_grid)
    return new_grid


def part2(points, folds):
    """
    Finish folding the transparent paper according to the instructions.
    The manual says the code is always eight capital letters.

    What code do you use to activate the infrared thermal imaging camera system?
    """
    # find the biggest x and y values
    bigx, bigy = 0, 0
    for coords in points:
        x = coords[0]
        y = coords[1]
        if x > bigx:
            bigx = x
        if y > bigy:
            bigy = y

    # generate the empty grid
    grid = {}
    for iy in range(bigy + 1):
        grid[iy] = ["." for ix in range(bigx + 1)]

    # draw the points on the grid
    for coords in points:
        x = coords[0]
        y = coords[1]
        grid[y][x] = "#"

    # perform all of the folds
    for fold in folds:
        fold_axis = fold[0]
        fold_line = fold[1]

        if fold_axis == "y":
            grid = fold_up_along_y(grid, fold_line)
        elif fold_axis == "x":
            grid = fold_left_along_x(grid, fold_line)

    # print out the grid - should see 8 ASCII capital letters
    print("Part 2 - final grid:")
    for line in grid:
        print("".join(grid[line]))


if __name__ == "__main__":
    points, folds = load_data()
    print(f"Points: {points}")
    print(f"Folds: {folds}")

    print(f"\nPart 1: {part1(points, folds)}\n")
    part2(points, folds)
