"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8

summary: string deduction

Part 1: 392
Part 2: 1004688
"""
from copy import deepcopy

def load_data():
    #datafile = 'input-day8-example'
    datafile = 'input-day8'
    data = []
    with open(datafile, 'r') as input:
        for line in input:
            patterns_and_values = line.strip().split(" | ")
            signal_patterns = patterns_and_values[0].split()
            output_values = patterns_and_values[1].split()
            data.append([signal_patterns, output_values])

    return data


def part1(data):
    """
    Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g
    There are ten unique signal patterns:

      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

    Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value
    Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are)

    In the output values, how many times do digits 1, 4, 7, or 8 appear?
    """
    count_1478 = 0
    for item in data:
        for output_value in item[1]:
            if len(output_value) in [2, 3, 4, 7]:
                count_1478 += 1

    return count_1478


def part2(data):
    """
    Solve for all 10 digits (0 - 9), then use the map of signals to numbers to figure out the output values
    What do you get if you add up all of the output values?

    Hmm I should try itertools.permutations 
    """
    total_output_value = 0
    for item in data:
        signal_map = map_signal_patterns(item[0])
        total_output_value += compute_output_value(item[1], signal_map)
    return total_output_value


def map_signal_patterns(signal_patterns):
    number_map = {}
    
    # First, solve for 1/4/7/8
    for pattern in signal_patterns:
        p = "".join(sorted(pattern))
        if len(p) == 2:
            number_map["1"] = p
        elif len(p) == 4:
            number_map["4"] = p
        elif len(p) == 3:
            number_map["7"] = p
        elif len(p) == 7:
            number_map["8"] = p

    # Now that we know 1 and 4, we can use that knowledge to solve for the remaining numbers
    for pattern in signal_patterns:
        p = "".join(sorted(pattern))

        # length 6 can be a 0, 6, or 9
        if len(p) == 6:
            # only 6 is not a superset of 1
            if number_map["1"][0] not in p or number_map["1"][1] not in p:
                number_map["6"] = p

            # only 9 is a superset of 4
            else:
                is_nine = True
                for char in number_map["4"]:
                    if char not in p:
                        is_nine = False
                
                if is_nine:
                    number_map["9"] = p
                else:
                    number_map["0"] = p

        # length 5 can be a 2, 3, or 5
        elif len(p) == 5:
            # only 3 is a superset of 1
            if number_map["1"][0] in p and number_map["1"][1] in p:
                number_map["3"] = p

            else:
                four_overlap_count = 0
                for char in number_map["4"]:
                    if char in p:
                        four_overlap_count += 1

                # 4 shares exactly three characters with a 5
                if four_overlap_count == 3:
                    number_map["5"] = p
                # 4 shares exactly two characters with a 5
                elif four_overlap_count == 2:
                    number_map["2"] = p
                else:
                    print("ERROR in 2/3/5 logic")

    # flip the keys and values in the number map to create the signal map
    signal_map = { number_map[x]: x for x in number_map}
    return signal_map


def compute_output_value(output_values, signal_map):
    final_value = ""
    for value in output_values:
        sorted_value = "".join(sorted(value))
        final_value += signal_map[sorted_value]
    return int(final_value)


if __name__ == '__main__':
    data = load_data()
    print(f"Data1: {data}\n")

    print(f"Part 1: {part1(deepcopy(data))}\n")
    print(f"Part 2: {part2(deepcopy(data))}\n")
