"""
day17b - https://adventofcode.com/2020/day/17

--- Day 17: Conway Cubes ---

* Part 2

Example: 848

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space.
How many cubes are left in the active state after the sixth cycle?
2000

"""
def load_data():
    y = []
    datafile = 'input-day17'
    #datafile = 'input-day17-example'
    with open(datafile, 'r') as input:
        for line in input:
            # add each x to the beginning of y
            y.insert(0, line.strip())

    # nest y inside an empty z inside an empty w
    dimension = [[y]]

    return dimension


def part2(dim):
    cycle = 1
    while cycle <= 6:
        pad_dim = create_padded_dimension(dim)
        dim = process_dimension(pad_dim)
        print(f"\n##### cycle {cycle} ######")
        cycle += 1

    active_cubes = 0
    for w in dim:
        for z in w:
            for y in z:
                for x in y:
                    if x == "#":
                        active_cubes += 1
    return active_cubes


def create_padded_dimension(dim):
    # gin up blank x/y/x parts that will be used to construct the padded dimension
    num_z = len(dim[0]) + 2
    num_y = len(dim[0][0]) + 2
    num_x = len(dim[0][0][0]) + 2

    blank_x = ""
    while len(blank_x) < num_x:
        blank_x += "."

    blank_y = [blank_x for i in range(num_y)]

    blank_z = [blank_y for i in range(num_z)]

    # assemble the padded dimension
    pad_dim = []
    pad_dim.append(blank_z)

    for w in dim:
        pad_z = []
        pad_z.append(blank_y)

        for z in w:
            pad_y = []
            pad_y.append(blank_x)
            for y in z:
                #print(y)
                pad_y.append("." + y + ".")
            pad_y.append(blank_x)
            pad_z.append(pad_y)

        pad_z.append(blank_y)
        pad_dim.append(pad_z)

    pad_dim.append(blank_z)

    return pad_dim


def process_dimension(pad_dim):
    # evaluate the padded dimension to create the new dimension
    new_dim = []
    for wloc in range(len(pad_dim)):
        w = pad_dim[wloc]
        new_dim_w = []

        for zloc in range(len(w)):
            z = w[zloc]
            new_dim_z = []

            for yloc in range(len(z)):
                y = z[yloc]
                new_dim_y = ""

                for xloc in range(len(y)):
                    x = y[xloc]
                    active_neighbors = check_neighbors(pad_dim, wloc, zloc, yloc, xloc)
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

            new_dim_w.append(new_dim_z)

        new_dim.append(new_dim_w)

    return new_dim


def check_neighbors(pad_dim, wloc, zloc, yloc, xloc):
    active_neighbors = 0

    wlist = [wloc]
    if wloc > 0:
        wlist.append(wloc-1)
    if wloc < len(pad_dim) - 1:
        wlist.append(wloc+1)

    zlist = [zloc]
    if zloc > 0:
        zlist.append(zloc-1)
    if zloc < len(pad_dim[0]) - 1:
        zlist.append(zloc+1)

    ylist = [yloc]
    if yloc > 0:
        ylist.append(yloc-1)
    if yloc < len(pad_dim[0][0]) - 1:
        ylist.append(yloc+1)

    xlist = [xloc]
    if xloc > 0:
        xlist.append(xloc-1)
    if xloc < len(pad_dim[0][0][0]) - 1:
        xlist.append(xloc+1)

    for w in wlist:
        for z in zlist:
            for y in ylist:
                for x in xlist:
                    if pad_dim[w][z][y][x] == "#":
                        active_neighbors += 1

    # subtract one if the center is active (it shouldn't be checked)
    if pad_dim[wloc][zloc][yloc][xloc] == "#":
        active_neighbors -= 1

    return active_neighbors


if __name__ == '__main__':
    data = load_data()
    print(f"data: {data}")

    results1 = part2(data)
    print(f"\nPart 2 - {results1}")
