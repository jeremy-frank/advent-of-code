"""
day3a - https://adventofcode.com/2020/day/3

You start on the open square (.) in the top-left corner and need to reach the bottom
(below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that
prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

..##.......
#...#...#..
.#....#..#.
..#.#...#x#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#


#....#........#............#...
..##....#..............#......#
..#......#.#.......####......#.

284
"""

def compute():
    hill = {}
    counter = 0

    datafile = 'input-day3'
    with open(datafile, 'r') as input:
        for line in input:
            hill[counter] = line.strip()
            counter += 1

    return navigate(hill)


def navigate(hill):
    trees = 0
    position = 0
    move_right = 3

    for key in hill:
        line = hill[key]

        print(f"position {position} on line {key}: {line}")
        if line[position] == "#":
            trees +=1

        position += move_right
        position %= len(line)

    return trees


if __name__ == '__main__':
    results = compute()
    print(results)
