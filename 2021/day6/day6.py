"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6

summary: track exponential growth of a school of fish

Part 1: 375482
Part 2: 1689540415957
"""
from copy import deepcopy
from pprint import pprint

def load_data():
    #datafile = 'input-day6-example'
    datafile = 'input-day6'
    with open(datafile, 'r') as input:
        for line in input:
            str_data = line.strip().split(",")
            data = [int(x) for x in str_data]
    return data


def part1(fish):
    """
    Each lanternfish creates a new lanternfish once every 7 days
    New lanternfish need an extra 2 days for their first cycle
    7-day timer is 0-6

    How many lanternfish would there be after 80 days?
    """
    for day in range(80):
        for i in range(len(fish)):
            if fish[i] > 0:
                fish[i] -= 1
            else:
                fish[i] = 6
                fish.append(8)

    return len(fish)


def part2(fish_list):
    """
    How many lanternfish would there be after 256 days?
    """
    fish = { i:0 for i in range(9) }
    for timer in fish_list:
        fish[timer] += 1

    for day in range(256):
        new_fish = { i:0 for i in range(9) }

        for timer in fish:
            if timer > 0:
                new_fish[timer-1] += fish[timer]
            else:
                new_fish[6] += fish[timer]
                new_fish[8] += fish[timer]

        fish = new_fish

    # pprint(fish)
    return sum(fish.values())


if __name__ == '__main__':
    data = load_data()
    print(f"Data: {data}\n")

    print(f"Part 1: {part1(deepcopy(data))}")
    print(f"Part 2: {part2(deepcopy(data))}\n")
