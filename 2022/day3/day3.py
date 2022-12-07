"""
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3

summary: compare strings to find duplicates

Part 1 - 7850
Part 2 - 2581
"""


def load_data():
    datafile = "input-day3"

    data = []
    with open(datafile, "r") as input:
        for line in input:
            data.append(line.strip())

    return data


def part1(rucksacks):
    """
    The Elves have made a list of all of the items currently in each rucksack
    Every item type is identified by a single lowercase or uppercase letter
      (that is, a and A refer to different types of items)

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

    Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    """
    priorities = {}
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = 0
    for item in items:
        priority += 1
        priorities[item] = priority

    score = 0
    for rucksack in rucksacks:
        half = int(len(rucksack) / 2)
        front = set(rucksack[:half])
        back = set(rucksack[half:])

        for char in front:
            if char in back:
                score += priorities[char]

    return score


def part2(rucksacks):
    """
    Every 3 lines is a group of elves. In that group, there will be exactly one item
     type (badge) that will be carried by all three elves.

    Find the item type that corresponds to the badges of each three-Elf group.
    What is the sum of the priorities of those item types?
    """
    priorities = {}
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = 0
    for item in items:
        priority += 1
        priorities[item] = priority

    counter = 0
    score = 0
    while counter < len(rucksacks):
        elf1 = set(rucksacks[counter])
        elf2 = set(rucksacks[counter + 1])
        elf3 = set(rucksacks[counter + 2])
        for char in elf1:
            if char in elf2 and char in elf3:
                score += priorities[char]
        counter += 3

    return score


if __name__ == "__main__":
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
