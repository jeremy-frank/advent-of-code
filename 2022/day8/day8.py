"""
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8

summary: traverse 2d grid of trees to determine which ones are visible from the edge

Part 1 - 1825
Part 2 - 235200
"""


def load_data():
    datafile = "input-day8"
    # datafile = "input-day8-example"

    data = []
    with open(datafile, "r") as input:
        for line in input:
            row = [int(x) for x in line.strip()]
            data.append(row)
    return data


def part1(forest):
    """
    Tree height: 0 is the shortest and 9 is the tallest
    A tree is visible if all of the other trees between it and and the
      edge of the grid are shorter than it

    Consider your map; how many trees are visible from outside the grid?
    """
    visible_trees = 0
    y_size = len(forest)
    x_size = len(forest[0])

    for y in range(y_size):
        for x in range(x_size):
            visible = check_tree_visibility(forest, x, y)
            if visible:
                visible_trees += 1

    return visible_trees


def check_tree_visibility(forest, x, y):
    my_tree = forest[y][x]
    print(f"Checking visibility for tree {my_tree} ({x},{y})")

    # All edge trees are visible (not strictly needed as it can be handled below)
    if x == 0 or x == (len(forest[0]) - 1) or y == 0 or y == (len(forest) - 1):
        return True

    # Generate a set of trees in each direction
    treelines = {
        "north": {forest[y_north][x] for y_north in range(0, y)},
        "south": {forest[y_south][x] for y_south in range(y + 1, (len(forest)))},
        "east": set(forest[y][x + 1 :]),
        "west": set(forest[y][:x]),
    }

    # Generate a set of every tree size that is the same or bigger than my_tree
    big_trees = {size for size in range(my_tree, 10)}

    for direction in treelines:
        # If adding the lists together results in the same length as adding the sets together,
        #  there were no big trees in the tree line, and therefore my_tree is visible from the edge
        treeline = treelines[direction]
        if len([*big_trees, *treeline]) == len({*big_trees, *treeline}):
            print(f"  Tree {my_tree} ({x},{y}) is visible from the {direction}")
            return True

    return False


def part2(forest):
    """
    The Elves need to know the best spot to build their tree house

    To measure the viewing distance from a given tree, look up, down, left, and right
    Stop if you reach an edge or at the first tree that is the same height or taller
      than the tree under consideration.
    A tree's scenic score is found by multiplying together its viewing distance in each
      of the four directions (north * south * east * west)

    Consider each tree on your map. What is the highest scenic score possible for any tree?
    """
    max_scenic_score = 0
    y_size = len(forest)
    x_size = len(forest[0])

    for y in range(y_size):
        for x in range(x_size):
            tree_score = calculate_tree_score(forest, x, y)
            if tree_score > max_scenic_score:
                max_scenic_score = tree_score

    return max_scenic_score


def calculate_tree_score(forest, x, y):
    my_tree = forest[y][x]

    # All edge trees have a score of zero (not strictly needed as it can be handled below)
    if x == 0 or x == (len(forest[0]) - 1) or y == 0 or y == (len(forest) - 1):
        return 0

    # Generate a list of trees in each direction
    treelines = {
        "north": [forest[y_north][x] for y_north in range(0, y)],
        "south": [forest[y_south][x] for y_south in range(y + 1, (len(forest)))],
        "east": list(forest[y][x + 1 :]),
        "west": list(forest[y][:x]),
    }

    # Reverse north and west, since we want to walk outward from the center
    treelines["north"].reverse()
    treelines["west"].reverse()

    total_score = 1
    for direction in treelines:
        score = 0
        # Walk along each treeline until we bump into a tree that is too big
        for tree in treelines[direction]:
            score += 1
            if tree >= my_tree:
                break
        total_score *= score

    print(f"Score for {my_tree} ({x},{y}) - {total_score}")
    return total_score


if __name__ == "__main__":
    data = load_data()
    for row in data:
        print(row)

    results1 = part1(data)
    results2 = part2(data)

    print(f"Part 1 - {results1}")
    print(f"Part 2 - {results2}\n")
