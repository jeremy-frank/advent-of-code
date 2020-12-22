"""
day16ab - https://adventofcode.com/2020/day/16

--- Day 16: Ticket Translation ---

* Part 1
Three input files:
  the rules for ticket fields
  the numbers on your ticket
  the numbers on other nearby tickets

The rules for ticket fields specify a list of fields that exist somewhere on the ticket 
  and the valid ranges of values for each field

Start by determining which tickets are completely invalid;
these are tickets that contain values which aren't valid for any field

Example: 4 + 55 + 12 = 71

Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71

Consider the validity of the nearby tickets you scanned.
What is your ticket scanning error rate?
24980

* Part 2
Using the valid ranges for each field, determine what order the fields appear on the tickets.
The order is consistent between all tickets: if seat is the third field, it is the third field 
  on every ticket, including your ticket.

Once you work out which field is which, look for the six fields on your ticket that start with 
the word departure. What do you get if you multiply those six values together?

0: arrival track
1: duration
2: departure time
3: departure station
4: class
5: type
6: departure date
7: wagon
8: arrival platform
9: price
10: arrival location
11: row
12: departure platform
13: zone
14: arrival station
15: departure location
16: train
17: route
18: departure track
19: seat

809376774329

"""
def load_ticket():
    ticket = []
    #datafile = 'input-day16-ticket-example'
    datafile = 'input-day16-ticket'
    with open(datafile, 'r') as input:
        for line in input:
            bits = line.strip().split(",")
            for x in bits:
                ticket.append(int(x))

    return ticket 


def load_rules():
    # part1 - single list of all possible values
    rule_full_range = []

    # part2 - dictionary holding the individual rules
    rules = {}

    #datafile = 'input-day16-rules-example'
    datafile = 'input-day16-rules'
    with open(datafile, 'r') as input:
        for line in input:
            line = line.strip().replace(":", ",").replace(" or", ",")
            items = line.split(",")

            rule_range = []
            for numrun in [items[1], items[2]]:
                nums = numrun.split("-")
                for x in range(int(nums[0]), int(nums[1]) + 1):
                    rule_range.append(x)
                    rule_full_range.append(x)
            rules[items[0]] = rule_range

    rule_full_range.sort()

    return rules, set(rule_full_range)


def load_nearby_tickets():
    nearby_tickets = []
    #datafile = 'input-day16-nearby-tickets-example'
    datafile = 'input-day16-nearby-tickets'
    with open(datafile, 'r') as input:
        for line in input:
            bits = line.strip().split(",")
            nearby_tickets.append([int(x) for x in bits])
    return nearby_tickets


def part1(rule_range, nearby_tickets):
    invalid_values = []

    for ticket in nearby_tickets:
        for val in ticket:
            if val not in rule_range:
                invalid_values.append(val)

    return sum(invalid_values)


def validate_tickets(rule_range, nearby_tickets):
    valid_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for val in ticket:
            if val not in rule_range:
                valid = False
        if valid:
            valid_tickets.append(ticket)
        #else:
        #    print(f"Invalid ticket: {ticket}")
    return valid_tickets


def process_tickets(rules, tickets, my_ticket):
    # for each position, find all rules that could match it
    pos_matches = {}
    for pos in range(len(tickets[0])):
        pos_matches[pos] = []
        for rule in rules:
            rule_range = rules[rule]
            rule_match = True
            for ticket in tickets:
                if ticket[pos] not in rule_range:
                    rule_match = False
                    break
            
            if rule_match:
                print(f"{pos} {rule}")
                pos_matches[pos].append(rule)

    print(f"\n\npos_matches: {pos_matches}\n\n")

    # narrow it down - figure out which position maps to what rule
    pos_solution = {}
    solved_rule = []
    while len(pos_solution) < len(rules):
        new_pos_matches = {}
        for pos in pos_matches:
            if len(pos_matches[pos]) == 1:
                # found a solution! (add to pos_solution and not to new_pos_matches)
                pos_solution[pos] = pos_matches[pos][0]
                solved_rule.append(pos_matches[pos][0])
                print(f"updated pos_solution: {pos_solution}")
            elif len(pos_matches[pos]) == 0:
                # shouldn't ever happen
                print("ERROR")
            else:
                # no solution yet, so add anything that isn't yet solved to new_pos_matches
                new_pos_matches[pos] = []
                for item in pos_matches[pos]:
                    if item not in solved_rule:
                        new_pos_matches[pos].append(item)
        
        pos_matches = new_pos_matches

    # print out the full position:rule mapping
    print("\n")
    for x in range(len(pos_solution)):
        print(f"{x}: {pos_solution[x]}")

    # calculate the solution
    print("\n")
    answer = 1
    for pos in pos_solution:
        if "departure" in pos_solution[pos]:
            print(f"{pos} - {pos_solution[pos]}, ticket value {my_ticket[pos]}")
            answer *= my_ticket[pos]

    return answer


if __name__ == '__main__':
    my_ticket = load_ticket()
    print(f"my_ticket: {my_ticket} \n")

    rules, rule_range = load_rules()
    print(f"rules: {rules} \n")
    print(f"rule_range: {rule_range} \n")

    nearby_tickets = load_nearby_tickets()
    print(f"nearby_tickets: {nearby_tickets} \n")

    results1 = part1(rule_range, nearby_tickets)

    valid_tickets = validate_tickets(rule_range, nearby_tickets)
    results2 = process_tickets(rules, valid_tickets, my_ticket)

    print(f"\nPart 1 - {results1}")
    print(f"Part 2 - {results2}\n")
