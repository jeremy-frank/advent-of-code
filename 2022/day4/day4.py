"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4

summary: find range overlaps

Part 1 - 518
Part 2 - 909
"""


def load_data():
    datafile = "input-day4"

    data = []
    with open(datafile, "r") as input:
        for line in input:
            data.append(line.strip().split(","))

    return data


def part1(assignments):
    """
    Every section has a unique ID number, and each Elf is assigned a range of section IDs.
    They've noticed that many of the assignments overlap.

    In how many assignment pairs does one range fully contain the other?
    """
    full_overlap_count = 0
    for assignment in assignments:
        print(f"Checking assignment {assignment}")

        elf1_start, elf1_stop = assignment[0].split("-")
        elf1_set = {i for i in range(int(elf1_start), int(elf1_stop) + 1)}

        elf2_start, elf2_stop = assignment[1].split("-")
        elf2_set = {i for i in range(int(elf2_start), int(elf2_stop) + 1)}

        if elf1_set.issubset(elf2_set) or elf2_set.issubset(elf1_set):
            print("  Found a full overlap:")
            print(f"    elf1_set {elf1_set}")
            print(f"    elf2_set {elf2_set}")
            full_overlap_count += 1

    return full_overlap_count


def part2(assignments):
    """
    Instead, the Elves would like to know the number of pairs that overlap at all.
    In how many assignment pairs do the ranges overlap?
    """
    overlap_count = 0
    for assignment in assignments:
        elf1_start, elf1_stop = assignment[0].split("-")
        elf1_set = {i for i in range(int(elf1_start), int(elf1_stop) + 1)}

        elf2_start, elf2_stop = assignment[1].split("-")
        elf2_set = {i for i in range(int(elf2_start), int(elf2_stop) + 1)}

        overlap1 = False
        for section in elf1_set:
            if section in elf2_set:
                overlap1 = True

        if overlap1:
            overlap_count += 1
        else:
            overlap2 = False
            for section in elf2_set:
                if section in elf1_set:
                    overlap2 = True
            if overlap2:
                overlap_count += 1

    return overlap_count


if __name__ == "__main__":
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
