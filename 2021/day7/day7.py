"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7

summary: crab subs, number crunching to find lowest fuel cost

Part 1: 325528 (Value was 342)
Part 2: 85015836 (Value was 460)
"""
from copy import deepcopy
from statistics import mean

def load_data():
    #datafile = 'input-day7-example'
    datafile = 'input-day7'
    with open(datafile, 'r') as input:
        for line in input:
            str_data = line.strip().split(",")
            data = [int(x) for x in str_data]

    return sorted(data)


def part1(crabs):
    """
    Crab submarines can only move horizontally
    Find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible
    How much fuel must they spend to align to that position?
    """
    lowest_fuel_cost = 100000000
    for i in range(crabs[0], crabs[-1]+1):
        fuel_cost = 0

        for crab in crabs:
            fuel_cost += abs(crab - i)

        if fuel_cost < lowest_fuel_cost:
            lowest_fuel_cost = fuel_cost
            print(f"Value {i} produced a new low fuel cost of {lowest_fuel_cost}")

    return lowest_fuel_cost


def part2(crabs):
    """
    Each change of 1 step in horizontal position costs 1 more unit of fuel than the last: 
     the first step costs 1, the second step costs 2, the third step costs 3, and so on.
    How much fuel must they spend to align to that position?
    """
    crab_mean = int(mean(crabs))
    print(f"The mean of the list is {crab_mean}")

    fuel_cost = 0
    for crab in crabs:
        distance = abs(crab - crab_mean)
        for i in range(1, distance+1):
            fuel_cost += i

    return fuel_cost


if __name__ == '__main__':
    data = load_data()
    print(f"Data: {data}\n")

    print(f"Part 1: {part1(deepcopy(data))}")
    print(f"Part 2: {part2(deepcopy(data))}\n")
