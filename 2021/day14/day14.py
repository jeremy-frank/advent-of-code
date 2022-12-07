"""
--- Day 14: Extended Polymerization ---
https://adventofcode.com/2021/day/14

summary: exponential growth of polymer pairs (string)

Part 1: 2345
Part 2: 2432786807053
"""
from copy import deepcopy
from collections import defaultdict
from pprint import pprint


def load_data():
    # datafile = 'input-day14-example'
    datafile = "input-day14"
    rules = {}
    with open(datafile, "r") as input:
        for full_line in input:
            line = full_line.strip()
            if "->" in line:
                rule_bits = line.split(" -> ")
                rules[rule_bits[0]] = rule_bits[1]
            if line.isalpha():
                polymer = line

    return polymer, rules


def part1(polymer, rules):
    """
    Input is polymer template (string) and a list of pair insertion rules
    A rule like AB -> C means that when elements A and B are immediately adjacent,
      element C should be inserted between them.
    These insertions all happen simultaneously.
    Apply 10 steps of pair insertion to the polymer template
    Find the most and least common elements in the result
    Return quantity of the most common element - quantity of the least common element
    """
    for step in range(10):
        new_polymer = ""
        for i, p in enumerate(polymer):
            new_polymer += p
            if i < len(polymer) - 1:
                combo = p + polymer[i + 1]
                if combo in rules:
                    new_polymer += rules[combo]

        polymer = new_polymer
        # print(f"Step {step}: {polymer}")

    elements = defaultdict(int)
    for p in polymer:
        elements[p] += 1

    most_common_element, least_common_element = 0, 1000
    for element in elements:
        if elements[element] > most_common_element:
            most_common_element = elements[element]
        if elements[element] < least_common_element:
            least_common_element = elements[element]

    pprint(elements)
    return most_common_element - least_common_element


def part2(polymer, rules):
    """
    Same problem, but now apply 40 steps
    Slight problem: exponential growth, so the part 1 solution won't work
    Instead, create a dict to track letter pairs
    """
    # populate a dictionary with all the pairs from the original polymer string
    pair_tracker = defaultdict(int)
    for i, p in enumerate(polymer):
        if i < len(polymer) - 1:
            pair = p + polymer[i + 1]
            pair_tracker[pair] += 1

    for step in range(40):
        new_pair_tracker = defaultdict(int)
        for pair in rules:
            if pair in pair_tracker and pair_tracker[pair] > 0:
                new_pair1 = pair[0] + rules[pair]
                new_pair2 = rules[pair] + pair[1]
                count = pair_tracker[pair]
                new_pair_tracker[new_pair1] += count
                new_pair_tracker[new_pair2] += count
        pair_tracker = new_pair_tracker

    # count all the letters
    elements = defaultdict(int)
    for pair in pair_tracker:
        # just need the first letter of each pair
        elements[pair[0]] += pair_tracker[pair]

    # add the final character from the original polymer (it got missed in the above counting)
    elements[polymer[-1]] += 1

    most_common_element, least_common_element = 0, 0
    for element in elements:
        if elements[element] > most_common_element:
            most_common_element = elements[element]
        if elements[element] < least_common_element or least_common_element == 0:
            least_common_element = elements[element]

    pprint(elements)
    return most_common_element - least_common_element


if __name__ == "__main__":
    polymer, rules = load_data()
    print(f"Polymer: {polymer}\n")
    print(f"Rules: {rules}\n")
    print(f"Part 1: {part1(deepcopy(polymer), rules)}\n")
    print(f"Part 2: {part2(deepcopy(polymer), rules)}\n")
