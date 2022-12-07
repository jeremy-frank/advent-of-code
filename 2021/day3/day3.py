"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3

summary: find most common / least common bits in binary strings

Part 1 - 4103154
Part 2 - 4245351
"""
from copy import deepcopy


def load_data():
    # datafile = 'input-day3-example'
    datafile = "input-day3"
    data = []
    with open(datafile, "r") as input:
        for line in input:
            data.append(line.strip())

    return data


def part1(report):
    """
    Use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate)
    The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

    gamma rate: Find the most common bit in the corresponding position of all numbers in the diagnostic report
    epsilon rate: Find the least common bit in each position
    """
    gamma = ""
    epsilon = ""

    for pos in range(len(report[0])):
        # count the zeros and ones in the current position
        zero_count = 0
        one_count = 0
        for line in report:
            if line[pos] == "0":
                zero_count += 1
            else:
                one_count += 1

        # evaluate the counts and determine what next value should be
        if zero_count > one_count:
            gamma += "0"
            epsilon += "1"
        elif one_count > zero_count:
            gamma += "1"
            epsilon += "0"
        else:
            print("ERROR: Same amount of zeros and ones!")

    # convert binary to decimal
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)

    return gamma_dec * epsilon_dec


def part2(report):
    """
    Verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating

    Start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers
    Keep only numbers selected by the bit criteria (see below)
    If you only have one number left, stop; this is the rating value for which you are searching.
    Otherwise, repeat the process, considering the next bit to the right

    Bit Criteria:
    Oxygen generator rating: determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position being considered

    CO2 scrubber rating: determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 0 in the position being considered
    """
    oxygen_rating = find_rating("oxygen", report)
    co2_rating = find_rating("co2", report)

    return oxygen_rating * co2_rating


def find_rating(rating_type, original_report):

    report = deepcopy(original_report)

    for pos in range(len(report[0])):
        # count the zeros and ones in the current position
        zero_count = 0
        one_count = 0
        for line in report:
            if line[pos] == "0":
                zero_count += 1
            else:
                one_count += 1

        # evaluate the counts and determine what the bad (unwanted) value is
        if (rating_type == "oxygen" and zero_count > one_count) or (
            rating_type == "co2" and zero_count <= one_count
        ):
            bad_val = "1"
        else:
            bad_val = "0"

        # remove unwanted items in the report
        for line in deepcopy(report):
            if line[pos] == bad_val:
                report.remove(line)

        # if there's only one item left, we've found it
        if len(report) == 1:
            # convert binary to decimal
            return int(report[0], 2)


if __name__ == "__main__":
    data = load_data()
    print(f"Data: {data}\n")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}\n")
