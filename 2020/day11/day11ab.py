"""
day11ab - https://adventofcode.com/2020/day/11

* Part 1

The seat layout fits neatly on a grid.
Each position is either floor (.), an empty seat (L), or an occupied seat (#).

All decisions are based on the number of occupied seats adjacent to a given seat
(one of the eight positions immediately up, down, left, right, or diagonal from the seat).

The following rules are applied to every seat simultaneously:
- If a seat is empty (L) and there are no occupied seats adjacent to it, 
  the seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
  the seat becomes empty.
- Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state.
How many seats end up occupied?
2361

* Part 2

People don't just care about adjacent seats - they care about the first seat they can see in 
each of those eight directions!

Example: 26

It now takes five or more visible occupied seats for an occupied seat to become empty
 (rather than four or more from the previous rules).
2119

"""
import copy

def load_data():
    data = []
    datafile = 'input-day11'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())
    return data


def process_data(area, advent_part):
    # keep checking seats until no seats change
    people_moved = True
    while people_moved:
        new_area = []
        for y in range(len(area)):
            new_area.append([])
            for x in range(len(area[y])):
                if area[y][x] == ".":
                    new_area[y].append(".")
                else:
                    if advent_part == "part1":
                        new_area[y].append(check_seat_part1(area, x, y, area[y][x]))
                    elif advent_part == "part2":
                        new_area[y].append(check_seat_part2(area, x, y, area[y][x]))

        if new_area == area:
            people_moved = False

        area = new_area

    # count occupied seats
    occupied_seats = 0
    for y in area:
        for x in y:
            if x == "#":
                occupied_seats += 1
    return occupied_seats


def check_seat_part1(area, x, y, seat_type):
    occupied_seats = 0

    # not the real lengths - they are one shorter to compare with indexes starting at 0
    xlength = len(area[y]) - 1
    ylength = len(area) - 1

    #left
    if x > 0:
        if area[y][x-1] == "#":
            occupied_seats += 1

    #right
    if x < xlength:
        if area[y][x+1] == "#":
            occupied_seats += 1

    #up
    if y > 0:
        if area[y-1][x] == "#":
            occupied_seats += 1

        #up-left
        if x > 0:
            if area[y-1][x-1] == "#":
                occupied_seats += 1

        #up-right
        if x < xlength:
            if area[y-1][x+1] == "#":
                occupied_seats += 1

    #down
    if y < ylength:
        if area[y+1][x] == "#":
            occupied_seats += 1

        #down-left
        if x > 0:
            if area[y+1][x-1] == "#":
                occupied_seats += 1

        #down-right
        if x < xlength:
            if area[y+1][x+1] == "#":
                occupied_seats += 1
    
    if seat_type == "L" and occupied_seats == 0:
        return "#"
    elif seat_type == "L":
        return "L"
    elif seat_type == "#" and occupied_seats >= 4:
        return "L"
    elif seat_type == "#":
        return "#"
    

def check_seat_part2(area, x, y, seat_type):
    occupied_seats = 0

    # not the real lengths - they are one shorter to compare with indexes starting at 0
    xlength = len(area[y]) - 1
    ylength = len(area) - 1

    #left
    if x > 0:
        xcount = x
        foundseat = False
        while xcount > 0 and not foundseat:
            xcount -= 1
            if area[y][xcount] == "#":
                occupied_seats += 1
                foundseat = True
            elif area[y][xcount] == "L":
                foundseat = True

    #right
    if x < xlength:
        xcount = x
        foundseat = False
        while xcount < xlength and not foundseat:
            xcount += 1
            if area[y][xcount] == "#":
                occupied_seats += 1
                foundseat = True
            elif area[y][xcount] == "L":
                foundseat = True

    #up
    if y > 0:
        ycount = y
        foundseat = False
        while ycount > 0 and not foundseat:
            ycount -= 1
            if area[ycount][x] == "#":
                occupied_seats += 1
                foundseat = True
            elif area[ycount][x] == "L":
                foundseat = True

        #up-left
        if x > 0:
            ycount = y
            xcount = x
            foundseat = False
            while ycount > 0 and xcount > 0 and not foundseat:
                ycount -= 1
                xcount -= 1
                if area[ycount][xcount] == "#":
                    occupied_seats += 1
                    foundseat = True
                elif area[ycount][xcount] == "L":
                    foundseat = True

        #up-right
        if x < xlength:
            ycount = y
            xcount = x
            foundseat = False
            while ycount > 0 and xcount < xlength and not foundseat:
                ycount -= 1
                xcount += 1
                if area[ycount][xcount] == "#":
                    occupied_seats += 1
                    foundseat = True
                elif area[ycount][xcount] == "L":
                    foundseat = True

    #down
    if y < ylength:
        ycount = y
        foundseat = False
        while ycount < ylength and not foundseat:
            ycount += 1
            if area[ycount][x] == "#":
                occupied_seats += 1
                foundseat = True
            elif area[ycount][x] == "L":
                foundseat = True


        #down-left
        if x > 0:
            ycount = y
            xcount = x
            foundseat = False
            while ycount < ylength and xcount > 0 and not foundseat:
                ycount += 1
                xcount -= 1
                if area[ycount][xcount] == "#":
                    occupied_seats += 1
                    foundseat = True
                elif area[ycount][xcount] == "L":
                    foundseat = True


        #down-right
        if x < xlength:
            ycount = y
            xcount = x
            foundseat = False
            while ycount < ylength and xcount < xlength and not foundseat:
                ycount += 1
                xcount += 1
                if area[ycount][xcount] == "#":
                    occupied_seats += 1
                    foundseat = True
                elif area[ycount][xcount] == "L":
                    foundseat = True

    
    if seat_type == "L" and occupied_seats == 0:
        return "#"
    elif seat_type == "#" and occupied_seats >= 5:
        return "L"
    else:
        return seat_type


if __name__ == '__main__':
    data = load_data()
    #print(data)

    results1 = process_data(copy.deepcopy(data), "part1")
    print(f"Part 1 - {results1}")

    results2 = process_data(copy.deepcopy(data), "part2")
    print(f"Part 2 - {results2}")
