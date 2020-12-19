"""
day12a - https://adventofcode.com/2020/day/12

* Part 1
The navigation instructions (your puzzle input) consists of a sequence of 
single-character actions paired with integer input values.

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing. 

Example: 17 + 8 = 25

Figure out where the navigation instructions lead.
What is the Manhattan distance between that location and the ship's starting position?
364

"""
import copy

def load_data():
    data = []
    datafile = 'input-day12'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())
    return data


def process_data(instructions):
    x = 0
    y = 0
    facing = "E"

    for i in instructions:
        action = i[0]
        num = int(i[1:])

        if action in ["N", "S", "E", "W"]:
            x, y = move_ship(x, y, action, num)
        elif action == "F":
            x, y = move_ship(x, y, facing, num)
        elif action in ["R", "L"]:
            facing = rotate_ship(facing, action, num)

    print(f"x {x}, y {y}")
    return abs(x) + abs(y)


def move_ship(x, y, action, num):
    if action == "N":
        y += num
    elif action == "S":
        y -= num
    elif action == "E":
        x += num
    elif action == "W":
        x -= num
    
    return x, y


def rotate_ship(facing, action, num):
    turns = int(num / 90)

    while turns > 4:
        turns -= 4
    
    if turns == 4:
        return facing

    compass = ["N", "E", "S", "W", "N", "E", "S", "W", "N", "E", "S", "W"]
    if facing == "N":
        location = 4
    elif facing == "E":
        location = 5
    elif facing == "S":
        location = 6
    elif facing == "W":
        location = 7
    
    if action == "R":
        location += turns
    elif action == "L":
        location -= turns

    return compass[location]


if __name__ == '__main__':
    data = load_data()
    print(data)

    results = process_data(copy.deepcopy(data))
    print(f"Part 1 - {results}")

    #results = process_data(copy.deepcopy(data), "part2")
    #print(f"Part 2 - {results}")
