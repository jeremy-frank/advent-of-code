"""
day2a - https://adventofcode.com/2020/day/2

* Part 1

Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear for
the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times.

How many passwords are valid according to their policies?
416
"""

def compute():
    validpasswords = 0

    datafile = 'input-day2'
    with open(datafile, 'r') as input:
        for line in input:
            cleanline = line.strip()
            minmax, letter, password = cleanline.split()
            min, max = minmax.split('-')
            letter = letter[0]

            if evaluate_password(min, max, letter, password):
                validpasswords += 1
                print(f"found a valid password: {cleanline}")

    return validpasswords


def evaluate_password(min, max, letter, password):
    lettercount = 0
    for char in password:
        if char == letter:
            lettercount += 1

    if lettercount >= int(min) and lettercount <= int(max):
        return True

    return False


if __name__ == '__main__':
    results = compute()
    print(results)
