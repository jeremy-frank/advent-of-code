"""
--- Day 9: Rope Bridge ---
https://adventofcode.com/2022/day/9

summary: follow the leader around a 2d grid

Part 1 - 6057
Part 2 - 2514
"""


def load_data():
    datafile = "input-day9"
    # datafile = "input-day9-example"
    # datafile = "input-day9-example2"

    data = []
    with open(datafile, "r") as input:
        for line in input:
            bits = line.strip().split(" ")
            data.append([bits[0], int(bits[1])])
    return data


def part1(instructions):
    """
    These knots mark the head and the tail of the rope
    The head (H) and tail (T) must always be touching
    Diagonally adjacent and even overlapping both count as touching

    If the head is ever two steps directly up, down, left, or right from the tail, 
     the tail must also move one step in that direction so it remains close enough
    If the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up

    Work out where the tail goes as the head follows a series of motions
    Assume the head and the tail both start at the same position, overlapping.

    Simulate your complete hypothetical series of motions.
    How many positions does the tail of the rope visit at least once?
    """
    tail_location = [0, 0]
    head_location = [0, 0]
    visited_positions = {"[0, 0]"}

    for i in instructions:
        direction = i[0]
        distance = i[1]
        for d in range(distance):
            head_location = move_head(head_location, direction)
            tail_location = move_tail(head_location, tail_location)
            visited_positions.add(str(tail_location))

    return len(visited_positions)


def move_head(head_location, direction):
    x = head_location[0]
    y = head_location[1]
    if direction == "U":
        return [x, y + 1]
    if direction == "D":
        return [x, y - 1]
    if direction == "R":
        return [x + 1, y]
    if direction == "L":
        return [x - 1, y]


def move_tail(head_location, tail_location):
    xhead = head_location[0]
    yhead = head_location[1]
    xtail = tail_location[0]
    ytail = tail_location[1]

    # touching or overlapping, no change
    if (abs(xhead - xtail) <= 1) and (abs(yhead - ytail) <= 1):
        return tail_location

    # same column, move up
    if xhead == xtail and yhead - ytail > 1:
        return [xtail, ytail + 1]

    # same column, move down
    if xhead == xtail and yhead - ytail < 1:
        return [xtail, ytail - 1]

    # same row, move right
    if yhead == ytail and xhead - xtail > 1:
        return [xtail + 1, ytail]

    # same row, move left
    if yhead == ytail and xhead - xtail < 1:
        return [xtail - 1, ytail]

    # move diagonal up/right
    if yhead - ytail > 0 and xhead - xtail > 0:
        return [xtail + 1, ytail + 1]

    # move diagonal up/left
    if yhead - ytail > 0 and xhead - xtail < 0:
        return [xtail - 1, ytail + 1]

    # move diagonal down/right
    if yhead - ytail < 0 and xhead - xtail > 0:
        return [xtail + 1, ytail - 1]

    # move diagonal down/left
    if yhead - ytail < 0 and xhead - xtail < 0:
        return [xtail - 1, ytail - 1]


def part2(instructions):
    """
    Now there are 10 knots, 1 head and 9 tails
    One knot is still the head of the rope and moves according to the series of
      motions. Each knot further down the rope follows the knot in front of it
      using the same rules as before.

    Simulate your complete series of motions on a larger rope with ten knots.
    How many positions does the tail of the rope visit at least once?
    """
    head_location = [0, 0]
    tail1_location = [0, 0]
    tail2_location = [0, 0]
    tail3_location = [0, 0]
    tail4_location = [0, 0]
    tail5_location = [0, 0]
    tail6_location = [0, 0]
    tail7_location = [0, 0]
    tail8_location = [0, 0]
    tail9_location = [0, 0]
    visited_positions = {"[0, 0]"}

    for i in instructions:
        direction = i[0]
        distance = i[1]
        for d in range(distance):
            head_location = move_head(head_location, direction)
            tail1_location = move_tail(head_location, tail1_location)
            tail2_location = move_tail(tail1_location, tail2_location)
            tail3_location = move_tail(tail2_location, tail3_location)
            tail4_location = move_tail(tail3_location, tail4_location)
            tail5_location = move_tail(tail4_location, tail5_location)
            tail6_location = move_tail(tail5_location, tail6_location)
            tail7_location = move_tail(tail6_location, tail7_location)
            tail8_location = move_tail(tail7_location, tail8_location)
            tail9_location = move_tail(tail8_location, tail9_location)
            visited_positions.add(str(tail9_location))

    return len(visited_positions)


if __name__ == "__main__":
    data = load_data()
    print(f"Data - {data}")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
