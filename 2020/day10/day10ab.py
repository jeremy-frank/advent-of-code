"""
day10ab - https://adventofcode.com/2020/day/10

* Part 1
Each of your joltage adapters is rated for a specific output joltage (your puzzle input).

Any given adapter can take an input 1, 2, or 3 jolts lower than its rating 
and still produce its rated output joltage.

In addition, your device has a built-in joltage adapter rated for 3 jolts higher 
than the highest-rated adapter in your bag.

Treat the charging outlet near your seat as having an effective joltage rating of 0.

Find a chain that uses all of your adapters to connect the charging outlet to your 
device's built-in adapter and count the joltage differences between the charging 
outlet, the adapters, and your device.

What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
2040

* Part 2
Figure out how many different ways they can be arranged.

What is the total number of distinct ways you can arrange the adapters to connect the 
charging outlet to your device?
28346956187648

"""
def load_data():
    data = [0]
    datafile = 'input-day10'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(int(line.strip()))
    data.sort()
    data.append(max(data) + 3)
    return data


def compare_adapters(adapters):
    """Part 1"""
    jolt1 = 0
    jolt3 = 0
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        if diff == 1:
            jolt1 += 1
        if diff == 3:
            jolt3 += 1
    print(f"Found {jolt1} jolt1 and {jolt3} jolt3")
    return jolt1 * jolt3


def find_combos_brute_force(adapters, position):
    """Part 2 - recursion, too slow"""
    if position == len(adapters) - 1:
        return 1

    else:
        answer = 0
        for new_position in range(position + 1, len(adapters)):
            if adapters[new_position] - adapters[position] <= 3:
                answer += find_combos_brute_force(adapters, new_position)
        return answer


cache = {}
def find_combos_global_cache(adapters, position):
    """Part 2 - recursion, using dynamic programming (cache/memoization)"""

    # successful combo - we made it to the end!
    if position == len(adapters) - 1:
        return 1
    
    # if the value is in the cache, grab it
    elif position in cache:
        return cache[position]

    # if it's not in the cache, do the work
    else:
        answer = 0
        for new_position in range(position + 1, len(adapters)):
            if adapters[new_position] - adapters[position] <= 3:
                answer += find_combos_global_cache(adapters, new_position)
        # cache the answer to avoid extra computation (no need to traverse this combo tree any more)
        cache[position] = answer
        return answer


def find_combos_internal_cache(adapters, position, cache):
    """Part 2 - recursion, using dynamic programming (cache/memoization) - wrote this afterwards"""

    # successful combo - we made it to the end!
    if position == len(adapters) - 1:
        return 1, cache
    
    # if the value is in the cache, grab it
    elif position in cache:
        return cache[position], cache

    # if it's not in the cache, do the work
    else:
        answer = 0
        for new_position in range(position + 1, len(adapters)):
            if adapters[new_position] - adapters[position] <= 3:
                this_answer, cache = find_combos_internal_cache(adapters, new_position, cache)
                answer += this_answer
                cache[position] = answer
        return answer, cache


if __name__ == '__main__':
    data = load_data()
    print(data)

    jolts = compare_adapters(data)
    print(f"Part 1 - {jolts}")

    combos = find_combos_global_cache(data, 0)
    print(f"Part 2, global cache   - {combos}")

    combos, cache = find_combos_internal_cache(data, 0, {})
    print(f"Part 2, internal cache - {combos}")
