"""
day13ab - https://adventofcode.com/2020/day/13

--- Day 13: Shuttle Search ---

* Part 1
The first line is your estimate of the earliest timestamp you could depart on a bus.

The second line lists the bus IDs that are in service according to the shuttle company;
Entries that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you can 
take to the airport.


What is the ID of the earliest bus you can take to the airport 
multiplied by the number of minutes you'll need to wait for that bus?
222

* Part 2
The first line in your input is no longer relevant.

7,13,x,x,59,x,31,19
An x in the schedule means there are no constraints on what bus IDs must depart at that time.
This means you are looking for the earliest timestamp (called t) such that:
- Bus ID 7 departs at timestamp t.
- Bus ID 13 departs one minute after timestamp t.
- There are no requirements or restrictions on departures at two or three minutes after timestamp t.
- Bus ID 59 departs four minutes after timestamp t.
- There are no requirements or restrictions on departures at five minutes after timestamp t.
- Bus ID 31 departs six minutes after timestamp t.
- Bus ID 19 departs seven minutes after timestamp t.

The only bus departures that matter are the listed bus IDs at their specific offsets from t.
Those bus IDs can depart at other times, and other bus IDs can depart at those times.

Example: 1068781

Here are some other examples:
The earliest timestamp that matches the list 17,x,13,19 is 3417.
67,7,59,61 first occurs at timestamp 754018.
67,x,7,59,61 first occurs at timestamp 779210.
67,7,x,59,61 first occurs at timestamp 1261476.
1789,37,47,1889 first occurs at timestamp 1202161486.

What is the earliest timestamp such that all of the listed bus IDs depart at 
offsets matching their positions in the list?
408270049879073

"""
def load_data():
    data = []
    datafile = 'input-day13'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())

    timestamp = int(data[0])

    buses = []
    for bus in data[1].split(","):
        if bus == "x":
            buses.append(1)
        else:
            buses.append(int(bus))
    
    return timestamp, buses


def part1(timestamp, buses):
    # arbitrary large number
    time_diff = 1000000

    for bus in buses:
        if bus != 1:
            previous_bus = timestamp % bus
            new_time_diff = bus - previous_bus

            if new_time_diff < time_diff:
                time_diff = new_time_diff
                best_bus = bus

    print(f"best_bus is {best_bus} and the time_diff is {time_diff}")
    return best_bus * time_diff


def part2(buses):
    """
    See https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    Think about it like prime numbers:
    - The first number that is divisible by both 5 and 7 is 35 (5*7)
    - The first number that is divisible by 5, 7, and 13 is 455 (5*7*13)
      Note that 455 is also divisible by 5*7, 5*13, and 7*13
    - Therefore, as soon as we find a timestamp that is evenly divisible by the current bus,
        we can multiply timejump by the bus and keep moving forward in bigger increments.
    """

    timestamp = 0
    timejump = 1
    for i, bus in enumerate(buses):
        # keep increasing timestamp until modulus is zero
        while (timestamp+i) % bus:
            timestamp += timejump
        timejump *= bus
        print(f"timejump is {timejump}")
    return timestamp


if __name__ == '__main__':
    timestamp, buses = load_data()
    print(f"Timestamp: {timestamp}")
    print(f"Buses: {buses}\n")

    results1 = part1(timestamp, buses)
    results2 = part2(buses)

    print(f"Part 1 - {results1}")
    print(f"Part 2 - {results2}")
