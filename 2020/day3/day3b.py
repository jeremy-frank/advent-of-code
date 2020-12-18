"""
day3b - https://adventofcode.com/2020/day/3

You start on the open square (.) in the top-left corner and need to reach the bottom
(below the bottom-most row on your map).

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

found 64 trees with move_right 1 and move_down 1
found 284 trees with move_right 3 and move_down 1
found 71 trees with move_right 5 and move_down 1
found 68 trees with move_right 7 and move_down 1
found 40 trees with move_right 1 and move_down 2
3510149120
"""

def compute():
    hill = {}
    counter = 0

    datafile = 'input-day3'
    with open(datafile, 'r') as input:
        for line in input:
            hill[counter] = line.strip()
            counter += 1

    trees = 1
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for slope in slopes:
        trees *= navigate(hill, slope[0], slope[1])
    return trees


def navigate(hill, move_right=3, move_down=1):
    trees = 0
    position = 0

    for key in hill:
        line = hill[key]

        if key == 0 or key % move_down == 0:
            #print(f"position {position} on line {key}: {line}")
            if line[position] == "#":
                trees +=1

            position += move_right
            position %= len(line)

    print(f"found {trees} trees with move_right {move_right} and move_down {move_down}")
    return trees


if __name__ == '__main__':
    results = compute()
    print(results)
