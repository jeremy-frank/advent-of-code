"""
day1ab - https://adventofcode.com/2020/day/1

Part 1 - 1019571
Part 2 - 100655544
"""

def load_data():
    numbers = []
    datafile = 'input-day1'
    with open(datafile, 'r') as input:
        for line in input:
            num = line.strip()
            numbers.append(int(num))
    
    return numbers


def part1(numbers):
    position = 0
    for first in numbers:
        for second in numbers[position:]:
            if first + second == 2020:
                print(f"found it: {first} * {second} = {first * second}")
                return first * second
        position += 1


def part2(numbers):
    position = 0
    for first in numbers:
        for second in numbers[position:]:
            position3 = position + 1
            for third in numbers[position3:]:
                if first + second + third == 2020:
                    print(f"found it: {first} * {second} * {third} = {first * second * third}")
                    return first * second * third
        position += 1


if __name__ == '__main__':
    data = load_data()
    print(f"{data} \n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
