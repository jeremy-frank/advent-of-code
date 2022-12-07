"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1

summary: track depth changes

Part 1 - 1266
Part 2 - 1217
"""


def load_data():
    data = []
    datafile = "input-day1"
    with open(datafile, "r") as input:
        for line in input:
            num = line.strip()
            data.append(int(num))

    return data


def part1(depths):
    """
    Count the number of times a depth measurement increases from the previous measurement
    How many measurements are larger than the previous measurement?
    """
    depth_increases = 0
    previous_depth = depths[0]
    for depth in depths:
        if depth > previous_depth:
            depth_increases += 1
        previous_depth = depth

    return depth_increases


def part2(depths):
    """
    Use the sum of 3-value windows to determine if the depth has increased or not
    If there are not at least 3 values left, stop
    """
    depth_increases = 0
    previous_depth_sum = depths[0] + depths[1] + depths[2]

    for i in range(len(depths)):
        if i + 2 >= len(depths):
            return depth_increases
        current_depth_sum = depths[i] + depths[i + 1] + depths[i + 2]
        if current_depth_sum > previous_depth_sum:
            depth_increases += 1
        previous_depth_sum = current_depth_sum


if __name__ == "__main__":
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
