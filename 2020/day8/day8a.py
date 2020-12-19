"""
day8a - https://adventofcode.com/2020/day/8

* Part 1

The boot code is represented as a text file with one instruction per line of text. Each instruction consists 
of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

* acc increases or decreases a single global value called the accumulator by the value given in the argument. 
For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, 
the instruction immediately below it is executed next.

* jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument 
as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue 
to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.

* nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

This is an infinite loop: with this sequence of jumps, the program will run forever. 
The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, 
what value is in the accumulator?
1331

"""
def load_data():
    code = []
    datafile = 'input-day8'
    with open(datafile, 'r') as input:
        for line in input:
            parts = line.strip().split()
            code.append([parts[0], int(parts[1])])
    return code


def process_data(code):
    accumulator = 0
    location = 0
    visited_locations = []

    while True:
        # check for infinite loop
        if location in visited_locations:
            return accumulator
        
        line = code[location]
        visited_locations.append(location)
        if line[0] == "acc":
            accumulator += line[1]
            location += 1

        elif line[0] == "jmp":
            location += line[1]

        elif line[0] == "nop":
            location += 1


if __name__ == '__main__':
    data = load_data()
    print(data)

    results = process_data(data)
    print(results)
