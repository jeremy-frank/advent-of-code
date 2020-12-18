# day5ab - https://adventofcode.com/2020/day/5

"""
* Part 1
This airline uses binary space partitioning to seat people.
A seat might be specified like FBFBBFFRLR, where
F means "front"
B means "back"
L means "left"
R means "right"

The first 7 characters will either be F or B; these specify exactly one of the 128
rows on the plane (numbered 0 through 127). Each letter tells you which half of a
region the given seat is in. Start with the whole list of rows; the first letter
indicates whether the seat is in the front (0 through 63) or the back (64 through 127).
The next letter indicates which half of that region the seat is in, and so on until you're
left with exactly one row.

The last three characters will be either L or R; these specify exactly one of the 8 columns
of seats on the plane (numbered 0 through 7). The same process as above proceeds again,
this time with only three steps. L means to keep the lower half, while R means to keep
the upper half.

Examples:
FBFBBFFRLR: row 44, column 5, seat ID
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.

Look through your list of boarding passes.
What is the highest seat ID on a boarding pass?
896

* Part 2
Find the missing seat

It's a completely full flight, so your seat should be the only missing boarding pass
in your list. However, there's a catch: some of the seats at the very front and back
of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though;
The seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
659
"""

def load_tickets():
    tickets = []
    datafile = 'input-day5'
    with open(datafile, 'r') as input:
        for line in input:
            tickets.append(line.strip())
    return tickets


def process_tickets(tickets):
    seats = []
    for ticket in tickets:
        row = get_spot(ticket[:-3], 128)
        col = get_spot(ticket[-3:], 8)
        seat_id = (row * 8) + col
        seats.append(seat_id)

    seats.sort()
    return seats


def get_spot(input, quantity):
    spots = [x for x in range(quantity)]
    for x in input:
        half = int(len(spots) / 2)
        if x == "F" or x == "L":
            spots = spots[:half]
        elif x == "B" or x == "R":
            spots = spots[half:]
    return spots[0]


def find_missing_seat(seats):
    for seat in seats:
        if (seat + 1) not in seats:
            return(seat + 1)


if __name__ == '__main__':
    tickets = load_tickets()
    seats = process_tickets(tickets)
    missing_seat = find_missing_seat(seats)

    #print(seats)
    print(f"The highest seat ID is {seats[-1]}")
    print(f"The missing seat ID is {missing_seat}")
