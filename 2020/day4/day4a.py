"""
day4a - https://adventofcode.com/2020/day/4

* Part 1

The expected fields are as follows:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Count the number of valid passports - those that have all required fields.
Treat cid as optional.

In your batch file, how many passports are valid?
"""

def load_data():
    passports = {}
    passport_id = 1
    passports[1] = {}

    datafile = 'input-day4'
    with open(datafile, 'r') as input:
        for line in input:
            cleanline = line.strip()
            # if it's an empty line, move on to the next passport
            if cleanline == "":
                passport_id += 1
                passports[passport_id] = {}
            # otherwise, add the fields from this line to the current passport
            else:
                for chunk in cleanline.split():
                    fieldval = chunk.split(':')
                    passports[passport_id][fieldval[0]] = fieldval[1]

    return passports


def validate_passports(passports):
    valid_passports = 0

    for passport in passports:
        required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for field in passports[passport]:
            if field in required_fields:
                required_fields.remove(field)
        if required_fields == []:
            valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    passports = load_data()
    results = validate_passports(passports)
    print(f"found {results} valid passports")
