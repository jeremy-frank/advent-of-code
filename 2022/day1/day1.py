"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1

summary: track which elves are carrying the most calories

Part 1 - 71471
Part 2 - 211189
"""


def load_data():
    datafile = "input-day1"

    data = []
    cal_total = 0
    with open(datafile, "r") as input:
        for line in input:
            val = line.strip()
            if val:
                cal_total += int(val)
            else:
                data.append(cal_total)
                cal_total = 0

    data.sort()
    return data


def part1(calories):
    """
    Find the Elf carrying the most Calories.
    How many total Calories is that Elf carrying?
    """
    return calories[-1]


def part2(calories):
    """
    Find the top three Elves carrying the most Calories.
    How many Calories are those Elves carrying in total?
    """
    top3_elves = calories[-3:]
    return sum(top3_elves)


if __name__ == "__main__":
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
