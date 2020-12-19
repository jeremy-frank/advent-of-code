"""
day12b - https://adventofcode.com/2020/day/12

* Part 2

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) 
         the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) 
         the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north

The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

Example: 214 + 72 = 286

Figure out where the navigation instructions actually lead.
What is the Manhattan distance between that location and the ship's starting position?
39518

"""
def load_data():
    data = []
    datafile = 'input-day12'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())
    return data


def process_data(instructions):
    shipx = 0
    shipy = 0
    wpx = 10
    wpy = 1

    for i in instructions:
        action = i[0]
        num = int(i[1:])

        if action in ["N", "S", "E", "W"]:
            wpx, wpy = move_waypoint(wpx, wpy, action, num)
            print(f"Moved waypoint to x {wpx}, y {wpy}")

        elif action in ["R", "L"]:
            wpx, wpy = rotate_waypoint(wpx, wpy, action, num)
            print(f"Rotated waypoint to x {wpx}, y {wpy}")

        if action == "F":
            shipx += (wpx * num)
            shipy += (wpy * num)
            print(f"Moved ship to x {shipx}, y {shipy}")

    print(f"\nFinal Waypoint: x {wpx}, y {wpy}")
    print(f"Final Ship: x {shipx}, y {shipy}\n")
    return abs(shipx) + abs(shipy)


def move_waypoint(x, y, action, num):
    if action == "N":
        y += num
    elif action == "S":
        y -= num
    elif action == "E":
        x += num
    elif action == "W":
        x -= num
    return x, y


def rotate_waypoint(wpx, wpy, action, num):
    """Welcome to the "draw rotation with pen & paper, stare at paper, 
       then convert to code" section"""

    turns = int(num / 90)

    while turns > 4:
        turns -= 4
    
    if turns == 4:
        return wpx, wpy
    
    if wpx == 0 and wpy == 0:
        return wpx, wpy

    quadrants = ["NE", "SE", "SW", "NW"]
    # figure out current quadrant
    if wpx >= 0 and wpy >= 0:
        location = 0 # NE
    elif wpx >= 0 and wpy <= 0:
        location = 1 # SE
    elif wpx <= 0 and wpy <= 0:
        location = 2 # SW
    elif wpx <= 0 and wpy >= 0:
        location = 3 # NW

    # rotate to new quadrant   
    if action == "R":
        location = (location + turns) % 4
    elif action == "L":
        location -= (location - turns + 4) % 4

    new_quadrant = quadrants[location]
    if turns == 2:
        # with 2 turns, we move to a diagonal quadrant, so x and y stay the same
        if new_quadrant == "NE":
            return abs(wpx), abs(wpy)
        elif new_quadrant == "SE":
            return abs(wpx), abs(wpy) * -1
        elif new_quadrant == "SW":
            return abs(wpx) * -1, abs(wpy) * -1
        elif new_quadrant == "NW":
            return abs(wpx) * -1, abs(wpy)
    else:
        # 1 or 3 turns is a move to an adjacent quadrant, so x and y get flipped
        if new_quadrant == "NE":
            return abs(wpy), abs(wpx)
        elif new_quadrant == "SE":
            return abs(wpy), abs(wpx) * -1
        elif new_quadrant == "SW":
            return abs(wpy) * -1, abs(wpx) * -1
        elif new_quadrant == "NW":
            return abs(wpy) * -1, abs(wpx)


if __name__ == '__main__':
    data = load_data()
    print(data)

    results = process_data(data)
    print(f"Part 2 - {results}")
