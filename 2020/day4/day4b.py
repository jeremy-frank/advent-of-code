"""
day4b - https://adventofcode.com/2020/day/4

* Part 2

You can continue to ignore the cid field, but each other field has strict rules
about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
  If cm, the number must be at least 150 and at most 193.
  If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present
and valid according to the above rules.

In your batch file, how many passports are valid?
"""

def load_passports():
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
            if field in required_fields and validate_field(field, passports[passport][field]):
                required_fields.remove(field)
        if required_fields == []:
            valid_passports += 1

    return valid_passports


def validate_field (field, val):
    # got lucky here that a few letters weren't thrown in to some of the int(val) fields,
    #   otherwise there would be tons of exceptions

    HCL_RULE = "0123456789abcdef"
    PID_RULE = "0123456789"

    if field == "byr" and 1920 <= int(val) <= 2002:
        return True

    elif field == "iyr" and 2010 <= int(val) <= 2020:
        return True

    elif field == "eyr" and 2020 <= int(val) <= 2030:
        return True

    elif field == "hgt":
        if len(val) >= 3 and val[-2:] == "cm" and 150 <= int(val[:-2]) <= 193:
            return True
        elif len(val) >= 3 and val[-2:] == "in" and 59 <= int(val[:-2]) <= 76:
            return True

    elif field == "hcl" and len(val) == 7 and val[0] == "#" and check_rule(HCL_RULE, val[1:]):
        return True

    elif field == "ecl" and val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True

    elif field == "pid" and len(val) == 9 and check_rule(PID_RULE, val):
        return True

    return False


def check_rule(rule, val):
    # aka "It's late and I don't want to deal with regex right now"
    for char in val:
        if char not in rule:
            return False
    return True


if __name__ == '__main__':
    passports = load_passports()
    results = validate_passports(passports)
    print(f"found {results} valid passports")
