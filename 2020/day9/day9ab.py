"""
day9ab - https://adventofcode.com/2020/day/9

* Part 1
XMAS starts by transmitting a preamble of 25 numbers.

After that, each number you receive should be the sum of any two of the 
25 immediately previous numbers. The two numbers will have different values, 
and there might be more than one such pair.

Example (using preamble of 5): 127

What is the first number that is not the sum of two of the 25 numbers before it?
556543474


* Part 2
You must find a contiguous set of at least two numbers in your list which sum to 
the invalid number from step 1.

Example: 62

Add together the smallest and largest number in this contiguous range
76096372

"""
import copy

def load_data():
    data = []
    datafile = 'input-day9'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(int(line.strip()))
    return data


def find_bad_number(data, preamble_length):
    """Part 1"""
    # populate the preamble
    preamble = [data.pop(0) for x in range(preamble_length)]

    while data:
        number = data[0]
        if not check_preamble(preamble, number):
            print(f"Found the first bad number: {number} cannot be created with {preamble}")
            return number
        else:
            preamble.append(data.pop(0))
            preamble.pop(0)


def check_preamble(preamble, number):
    for x in range(len(preamble)):
        firstnum = preamble[x]
        for secondnum in preamble[x+1:]:
            if firstnum + secondnum == number:
                return True
    return False


def find_weakness(data, target):
    """Part 2"""
    for x in range(len(data)):
        keep_adding = True
        target_attempt = 0
        solution = []
        counter = x

        while keep_adding:
            solution.append(data[counter])
            target_attempt += data[counter]

            if target_attempt == target and len(solution) > 1:
                solution.sort()
                print(f"Found the target: {target_attempt} can be created with {solution}")
                return solution[0] + solution[-1]
            elif target_attempt > target:
                keep_adding = False
            else:
                counter += 1


if __name__ == '__main__':
    data = load_data()
    # print(data)

    bad_number = find_bad_number(copy.deepcopy(data), 25)
    weakness = find_weakness(data, bad_number)

    print(f"Part 1 - The bad number is {bad_number}")
    print(f"Part 2 - The weakness is {weakness}")

