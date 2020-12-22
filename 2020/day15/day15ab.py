"""
day15a - https://adventofcode.com/2020/day/15

--- Day 15: Rambunctious Recitation ---

* Part 1
In this game, the players take turns saying numbers. 
They begin by taking turns reading from a list of starting numbers (your puzzle input). 
Then, each turn consists of considering the most recently spoken number:

- If that was the first time the number has been spoken, the current player says 0.
- Otherwise, the number had been spoken before; the current player announces how many 
  turns apart the number is from when it was previously spoken.
- So, after the starting numbers, each turn results in that player speaking aloud 
  either 0 (if the last number is new) or an age (if the last number is a repeat).

Example: 436
1 - 0
2 - 3
3 - 6
4 - 0
5 - 3
6 - 3
7 - 1
8 - 0
9 - 4
10 - 0

What will be the 2020th number spoken?
866

* Part 2
Determine the 30000000th number spoken
1437692

"""
import copy

def load_data():
    data = {}
    datafile = 'input-day15'
    with open(datafile, 'r') as input:
        for line in input:
            items = line.strip().split(",")

    turn = 0
    for item in items:
        turn += 1
        data[int(item)] = turn

    return data, turn


def process_data(nums, turn, max_turns):
    new_num = nums[turn]
    del nums[turn]

    while turn < max_turns:
        last_num = new_num
        last_turn = turn
        turn += 1

        if last_num not in nums:
            new_num = 0
            #print(f"turn {turn}, last_num {last_num} not found in nums {nums}")

        else:
            """
            grab the old turn number, then overwrite it with the new value
            there's no need for a list here, since we always have the second value (it's just turn - 1)
            this is the best-performing solution I found (about 8s)
            """
            old_turn = nums[last_num]
            new_num = last_turn - old_turn
            #print(f"turn {turn}, last_num {last_num} found in nums: {nums[last_num]}")

        nums[last_num] = last_turn

    return new_num


if __name__ == '__main__':
    data, turn = load_data()
    print(f"{data} \n")

    results1 = process_data(copy.deepcopy(data), turn, 2020)
    print(f"Part 1 - {results1}")

    results2 = process_data(copy.deepcopy(data), turn, 30000000)
    print(f"Part 2 - {results2}\n")
