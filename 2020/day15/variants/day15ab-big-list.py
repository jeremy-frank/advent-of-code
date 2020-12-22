"""
day15a - https://adventofcode.com/2020/day/15

"""
import copy

def load_data():
    data = {}
    datafile = 'input-day15'
    with open(datafile, 'r') as input:
        for line in input:
            items = line.strip().split(",")

    counter = 1
    for item in items:
        data[int(item)] = [counter]
        counter += 1

    return data


def process_data(nums, max_turns):
    turn = len(nums)

    # boo hack
    del nums[7]
    new_num = 7

    while turn < max_turns:
        last_num = new_num
        last_turn = turn
        turn += 1

        if last_num not in nums:
            nums[last_num] = [last_turn]
            new_num = 0
            #print(f"turn {turn}, last_num {last_num} not found in nums {nums}")

        else:
            """
            append the new number to an ever-growing list
            memory is free and infinite, right?
            it runs in about 23s
            """
            old_turn = nums[last_num][-1]
            nums[last_num].append(last_turn)
            new_num = last_turn - old_turn
            #print(f"turn {turn}, last_num {last_num} found in nums: {nums[last_num]}")

    return new_num


if __name__ == '__main__':
    data = load_data()
    print(f"{data} \n")

    results1 = process_data(copy.deepcopy(data), 2020)
    print(f"Part 1 - {results1}")

    results2 = process_data(copy.deepcopy(data), 30000000)
    print(f"Part 2 - {results2}\n")
