"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2

summary: process directions to calculate depth and horizontal position

Part 1 - 2322630
Part 2 - 2105273490
"""

def load_data():
    #datafile = 'input-day2-example'
    datafile = 'input-day2'
    data = []
    with open(datafile, 'r') as input:
        for line in input:
            line_list = line.split()
            line_list[1] = int(line_list[1])
            data.append(line_list)
    
    return data


def part1(commands):
    """
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.

    Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth
    """
    x = 0
    y = 0
    for command in commands:
        dir = command[0]
        num = command[1]
        if dir == "forward":
            x += num
        elif dir == "up":
            y -= num
        else:
            y += num
    
    return x * y


def part2(commands):
    """
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

    Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth
    """
    x = 0
    depth = 0
    aim = 0
    for command in commands:
        dir = command[0]
        num = command[1]
        if dir == "forward":
            x += num
            depth += aim * num
        elif dir == "up":
            aim -= num
        else:
            aim += num
    
    return x * depth


if __name__ == '__main__':
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
