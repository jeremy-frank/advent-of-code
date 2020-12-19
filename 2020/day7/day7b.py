"""
day7b - https://adventofcode.com/2020/day/7

* Part 2

Example 1: 32
Example 2: 126

How many individual bags are required inside your single shiny gold bag?
48160

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
                    subcontainers.append([subbag, int(itembits[0])])
                bags[primarybag] = subcontainers
            else:
                itembits = baglist[1].split(" ")
                bags[primarybag] = [
                    [f"{itembits[1]} {itembits[2]}", int(itembits[0])]
                ]

    return bags


def process_data(bags, this_bag,):
    # starting with a single shiny gold bag, recursively open bags until there are none left
    bag_count = 0

    contents = bags[this_bag]
    if contents == []:
        return 0
    
    for baglist in contents:
        new_bag = baglist[0]
        quantity = baglist[1]

        #for i in range(quantity):
        #    bag_count += 1 + process_data(bags, new_bag)

        bag_count += quantity * (1 + process_data(bags, new_bag))

    return bag_count


if __name__ == '__main__':
    data = load_data()
    results = process_data(data, "shiny gold")

    print(data)
    print(results)
