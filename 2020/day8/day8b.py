"""
day8b - https://adventofcode.com/2020/day/8

* Part 2

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
What is the value of the accumulator after the program terminates?
1121

"""
import copy

def load_data():
    code = []
    datafile = 'input-day8'
    with open(datafile, 'r') as input:
        for line in input:
            parts = line.strip().split()
            code.append([parts[0], int(parts[1])])
    return code


def process_data(code):
    for num in range(len(code)):
        line = code[num]
        print(f"investigating {num} - {line}")
        if line[0] == "acc":
            pass

        elif line[0] in ["jmp", "nop"]:
            tempcode = copy.deepcopy(code)

            if line[0] == "jmp":
                tempcode[num] = ["nop", line[1]]
            elif line[0] == "nop":
                tempcode[num] = ["jmp", line[1]]

            print(f"  - testing line {num} - changed jmp to {tempcode[num]}")
            accumulator, successful_test = run_code(tempcode)
            if successful_test:
                print(f"Success! changed line {num} - {line}")
                return accumulator


def run_code(code):
    accumulator = 0
    location = 0
    visited_locations = []

    while location < len(code):
        # failure! (infinite loop)
        if location in visited_locations:
            return accumulator, False

        line = code[location]
        visited_locations.append(location)
        if line[0] == "acc":
            accumulator += line[1]
            location += 1

        elif line[0] == "jmp":
            location += line[1]

        elif line[0] == "nop":
            location += 1

    # success!
    return accumulator, True


if __name__ == '__main__':
    data = load_data()
    print(data)

    results = process_data(data)
    print(results)
