"""
day2b - https://adventofcode.com/2020/day/2

* Part 2

Each policy actually describes two positions in the password, where 1 means the
first character, 2 means the second character, and so on. (Be careful; Toboggan
Corporate Policies have no concept of "index zero"!) Exactly one of these positions
must contain the given letter. Other occurrences of the letter are irrelevant for
the purposes of policy enforcement.

How many passwords are valid?
688
"""

def compute():
    validpasswords = 0

    datafile = 'input-day2'
    with open(datafile, 'r') as input:
        for line in input:
            cleanline = line.strip()
            minmax, letter, password = cleanline.split()
            positions = minmax.split('-')
            letter = letter[0]

            if evaluate_password(positions, letter, password):
                validpasswords += 1
                print(f"found a valid password: {cleanline}")

    return validpasswords


def evaluate_password(positions, letter, password):
    positioncount = 0

    for position in positions:
        if password[int(position)-1] == letter:
            positioncount += 1

    if positioncount == 1:
        return True

    return False


if __name__ == '__main__':
    results = compute()
    print(results)
