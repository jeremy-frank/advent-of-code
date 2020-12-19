"""
day7a - https://adventofcode.com/2020/day/7

* Part 1
bags must be color-coded and must contain specific quantities of other
color-coded bags

You have a shiny gold bag. If you wanted to carry it in at least one other bag,
how many different bag colors would be valid for the outermost bag?

Example: 4

In other words, how many bag colors can eventually contain at least one shiny gold bag?
287

"""

def load_data():
    bags = {}

    datafile = 'input-day7'
    with open(datafile, 'r') as input:
        for line in input:
            cleanline = line.strip()
            baglist = cleanline.split(" bags contain ")
            primarybag = baglist[0]

            if baglist[1] == "no other bags.":
                bags[primarybag] = []
            elif "," in baglist[1]:
                containlist = baglist[1].split(", ")
                subcontainers = []
                for item in containlist:
                    itembits = item.split(" ")
                    subbag = f"{itembits[1]} {itembits[2]}"
                    subcontainers.append(subbag)
                bags[primarybag] = subcontainers
            else:
                itembits = baglist[1].split(" ")
                bags[primarybag] = [f"{itembits[1]} {itembits[2]}"]

    return bags


def process_data(bags):
    shiny_gold_count = 0
    for bag in bags:
        if open_bag(bags, bag):
            shiny_gold_count += 1
    return shiny_gold_count


def open_bag(bags, bag):
    # recursively open bags until we find a shiny gold bag
    contents = bags[bag]
    if "shiny gold" in contents:
        return True
    elif contents == []:
        return False
    else:
        found_shiny_gold = False
        for item in contents:
            if open_bag(bags, item):
                found_shiny_gold = True
                break
        return found_shiny_gold


if __name__ == '__main__':
    data = load_data()
    results = process_data(data)

    #print(data)
    print(results)
