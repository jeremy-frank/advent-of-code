"""
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5

summary: simulate a crane moving crates between stacks

Part 1 - TQRFCBSJJ
Part 2 - RMHFJNVFP
"""

from copy import deepcopy


def load_stacks():
    datafile = "input-day5-stacks"
    # datafile = "input-day5-example-stacks"
    raw_stacks = []
    with open(datafile, "r") as input:
        for line in input:
            raw_stacks.append(line.rstrip())
    raw_stacks.reverse()

    # Use first line to determine number of stacks (assumes single digit number of stacks)
    stack_quantity = int(raw_stacks[0][-1])

    # Populate the dictionary with the appropriate number of stacks
    stacks = {}
    for i in range(1, stack_quantity + 1):
        stacks[i] = []

    # Skip the first line, and use the rest to construct the stacks
    for row in raw_stacks[1:]:
        column = 0
        spaces = 0
        for char in row:
            if char.isalpha():
                stacks[column].append(char)
            elif char == "[" or spaces >= 3:
                column += 1
                spaces = 0
            elif char == " ":
                spaces += 1

    return stacks


def load_instructions():
    datafile = "input-day5-instructions"
    # datafile = "input-day5-example-instructions"
    instructions = []
    with open(datafile, "r") as input:
        for line in input:
            parts = line.strip().split(" ")
            instructions.append(
                {
                    "quantity": int(parts[1]),
                    "origin": int(parts[3]),
                    "dest": int(parts[5]),
                }
            )

    return instructions


def part1(stacks, instructions):
    """
    The crane moves one crate at a time from the origin to the destination.
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    for i in instructions:
        quantity, origin, dest = i["quantity"], i["origin"], i["dest"]

        # Move crates one by one
        for q in range(quantity):
            crate = stacks[origin].pop(-1)
            stacks[dest].append(crate)

    # Assemble the answer by looking at the top of each stack
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]

    return answer


def part2(stacks, instructions):
    """
    The crane isn't a CrateMover 9000 - it's a CrateMover 9001!
    The crane has the ability to pick up and move multiple crates at once.
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    for i in instructions:
        quantity, origin, dest = i["quantity"], i["origin"], i["dest"]

        # Move crates in sets
        crates = stacks[origin][0 - quantity :]
        del stacks[origin][0 - quantity :]
        for crate in crates:
            stacks[dest].append(crate)

    # Assemble the answer by looking at the top of each stack
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]

    return answer


if __name__ == "__main__":
    stacks = load_stacks()
    print("\nStacks:")
    for stack in stacks:
        print(f"  {stack}: {stacks[stack]}")

    instructions = load_instructions()
    print("\nInstructions:")
    for instruction in instructions:
        print(f"  {instruction}")

    results1 = part1(deepcopy(stacks), instructions)
    print(f"Part 1 - {results1}")

    results2 = part2(deepcopy(stacks), instructions)
    print(f"Part 2 - {results2}\n")
