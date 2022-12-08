"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7

summary: recursively crawl a filesystem data structure and sum up disk space used

Part 1 - 1491614
Part 2 - 6400111
"""
from pprint import pprint

fs = {}


def load_data():
    datafile = "input-day7"
    # datafile = "input-day7-example"

    data = []
    with open(datafile, "r") as input:
        for line in input:
            data.append(line.strip())
    return data


def part1(data):
    """
    cd means change directory
      cd x moves in one level
      cd .. moves out one level
      cd / switches the current directory to the outermost directory, /
    ls means list
      123 abc means that the current directory contains a file named abc with size 123
      dir xyz means that the current directory contains a directory named xyz

    There are duplicate directory names!

    Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    """
    # build the filesystem tree
    current_path = ""
    for line in data:
        if line == "$ cd ..":
            current_path = fs[current_path]["parent"]

        elif line[:4] == "$ cd":
            parent = current_path

            if line[5:] == "/":
                current_path = "/"
            elif current_path == "/":
                current_path = f"/{line[5:]}"
            else:
                current_path = f"{current_path}/{line[5:]}"

            if current_path not in fs:
                fs[current_path] = {
                    "parent": parent,
                    "children": [],
                    "files": {},
                    "local_dir_size": 0,
                    "total_dir_size": 0,
                }

        elif line == "$ ls":
            pass

        elif line[:4] == "dir ":
            if current_path == "/":
                new_child = f"/{line[4:]}"
            else:
                new_child = f"{current_path}/{line[4:]}"
            fs[current_path]["children"].append(new_child)

        else:
            # everything else is a file
            filesize, filename = line.split(" ")
            fs[current_path]["local_dir_size"] += int(filesize)
            fs[current_path]["files"][filename] = int(filesize)

    fs["/"]["total_dir_size"] = get_size("/")
    pprint(fs)

    # sum up all directories with a size less than 100000
    total_10k_sizes = 0
    for directory in fs:
        if fs[directory]["total_dir_size"] <= 100000:
            total_10k_sizes += fs[directory]["total_dir_size"]

    return total_10k_sizes


def get_size(directory):
    # recursively calculate the total_dir_size of every directory
    total_child_size = 0
    for child in fs[directory]["children"]:
        print(f"get_size {directory} --> child {child}")
        total_child_size += get_size(child)
    fs[directory]["total_dir_size"] = fs[directory]["local_dir_size"] + total_child_size
    return fs[directory]["total_dir_size"]


def part2():
    """
    The total disk space available to the filesystem is 70000000.
    To run the update, you need unused space of at least 30000000.

    Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
    What is the total size of that directory?
    """
    free_space = 70000000 - fs["/"]["total_dir_size"]
    required_space = 30000000 - free_space
    closest_to_required_space = 70000000  # arbitrary large number to start

    for directory in fs:
        dir_size = fs[directory]["total_dir_size"]
        if dir_size >= required_space and dir_size < closest_to_required_space:
            closest_to_required_space = fs[directory]["total_dir_size"]

    return closest_to_required_space


if __name__ == "__main__":
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2()
    print(f"Part 2 - {results2}\n")
