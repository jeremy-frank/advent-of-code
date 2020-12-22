"""
day17a - https://adventofcode.com/2020/day/17

--- Day 17: Conway Cubes ---

* Part 1

There is an infinite 3-dimensional grid. 
At every integer 3-dimensional coordinate (x,y,z), 
  there exists a single cube which is either active or inactive

Almost all cubes start inactive

active (#) or inactive (.)

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors:
  any of the 26 other cubes where any of their coordinates differ by at most 1.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, 
  the cube remains active. Otherwise, the cube becomes inactive.

If a cube is inactive but exactly 3 of its neighbors are active, 
  the cube becomes active. Otherwise, the cube remains inactive.

Example: 112 cubes are in the active state after the 6th cycle

Starting with your given initial configuration, simulate six cycles.
How many cubes are left in the active state after the sixth cycle?
322

"""
import copy

def load_data():
    y = []
    datafile = 'input-day17'
    #datafile = 'input-day17-example'
    with open(datafile, 'r') as input:
        for line in input:
            # add each x to the beginning of y
            y.insert(0, line.strip())

    dimension = [y]

    # nest y inside an empty z
    return dimension


def part1(dim):
    cycle = 1
    while cycle <= 6:
        pad_dim = create_padded_dimension(dim)
        dim = process_dimension(pad_dim)
        print(f"\n##### cycle {cycle} ######")
        for z in dim:
            print("")
            for y in z:
                print(y)
        cycle += 1

    active_cubes = 0
    for z in dim:
        for y in z:
            for x in y:
                if x == "#":
                    active_cubes += 1
    return active_cubes


def create_padded_dimension(dim):
    # gin up blank x/y parts that will be used to construct the padded dimension
    num_y = len(dim[0]) + 2
    num_x = len(dim[0][0]) + 2

    blank_x = ""
    while len(blank_x) < num_x:
        blank_x += "."

    blank_y = [blank_x for i in range(num_y)]

    # assemble the padded dimension
    pad_dim = []

    # add blank z-1
    pad_dim.append(blank_y)

    # add all the existing stuff, with an extra blank y before and after
    for z in dim:
        pad_y = []
        pad_y.append(blank_x)
        for y in z:
            #print(y)
            pad_y.append("." + y + ".")
        pad_y.append(blank_x)
        pad_dim.append(pad_y)

    # add blank z+1
    pad_dim.append(blank_y)

    return pad_dim


def process_dimension(pad_dim):
    # evaluate the padded dimension to create the new dimension
    new_dim = []
    for zloc in range(len(pad_dim)):
        z = pad_dim[zloc]
        new_dim_z = []
        for yloc in range(len(z)):
            y = z[yloc]
            new_dim_y = ""
            for xloc in range(len(y)):
                x = y[xloc]
                active_neighbors = check_neighbors(pad_dim, zloc, yloc, xloc)
                if x == "#":
                    if active_neighbors in [2, 3]:
                        new_dim_y += "#"
                    else:
                        new_dim_y += "."
                elif x == ".":
                    if active_neighbors == 3:
                        new_dim_y += "#"
                    else:
                        new_dim_y += "."
            new_dim_z.append(new_dim_y)

        new_dim.append(new_dim_z)

    return new_dim


def check_neighbors(pad_dim, zloc, yloc, xloc):
    active_neighbors = 0

    zlist = [zloc]
    if zloc > 0:
        zlist.append(zloc-1)
    if zloc < len(pad_dim) - 1:
        zlist.append(zloc+1)

    ylist = [yloc]
    if yloc > 0:
        ylist.append(yloc-1)
    if yloc < len(pad_dim[0]) - 1:
        ylist.append(yloc+1)

    xlist = [xloc]
    if xloc > 0:
        xlist.append(xloc-1)
    if xloc < len(pad_dim[0][0]) - 1:
        xlist.append(xloc+1)

    for z in zlist:
        for y in ylist:
            for x in xlist:
                if pad_dim[z][y][x] == "#":
                    active_neighbors += 1

    # remove one if the center is active (it shouldn't be checked)
    if pad_dim[zloc][yloc][xloc] == "#":
        active_neighbors -= 1

    return active_neighbors


if __name__ == '__main__':
    data = load_data()
    print(f"data: {data} \n")

    results1 = part1(data)
    print(f"\nPart 1 - {results1}")
