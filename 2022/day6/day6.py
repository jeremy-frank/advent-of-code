"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6

summary: find the first set of x unique letters in a string

Part 1 - 1356
Part 2 - 2564
"""


def load_data():
    datafile = "input-day6"
    # datafile = "input-day6-example"

    with open(datafile, "r") as input:
        for line in input:
            return line.strip()


def part1(signal):
    """
    Malfunctioning device: the signal is a series of seemingly-random characters that the device receives one at a time.
    Add a subroutine to the device that detects a start-of-packet marker in the datastream
    The start of a packet is indicated by a sequence of four characters that are all different

    How many characters need to be processed before the first start-of-packet marker is detected?
    """
    for index in range(4, len(signal)):
        sequence = signal[index - 4 : index]
        if len(set(sequence)) == 4:
            print(f"Found {sequence} at position {index}")
            return index


def part2(signal):
    """
    It looks like it also needs to look for messages
    A start-of-message marker consists of 14 distinct characters (rather than 4)

    How many characters need to be processed before the first start-of-message marker is detected?
    """
    for index in range(14, len(signal)):
        sequence = signal[index - 14 : index]
        if len(set(sequence)) == 14:
            print(f"Found {sequence} at position {index}")
            return index


if __name__ == "__main__":
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
