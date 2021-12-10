"""
--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5

summary: draw lines on a 2d grid, count intersections

Part 1: 5197
Part 2: 18605
"""
from copy import deepcopy
from pprint import pprint

def load_data():
    #datafile = 'input-day5-example'
    datafile = 'input-day5'
    data = []
    with open(datafile, 'r') as input:
        for line in input:
            str_points = line.strip().replace(" -> ",",").split(",")
            points = [int(point) for point in str_points]
            data.append(points)
    return data


def part1_and_2(lines, draw_diagonal=False):
    """
    Part1: Consider only horizontal and vertical lines.
    Part2: Consider horizontal, vertical, *and* diagonal lines.
           All diagonal lines will be exactly 45 degrees

    At how many points do at least two lines overlap?
    """
    # create the empty graph
    graph = dict()
    for y in range(0,1000):
        graph[y] = [0 for x in range(1000)]

    # draw lines:
    for line in lines:
        x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
 
        # vertical line:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                graph[i][x1] += 1

        # horizontal line:
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                graph[y1][i] += 1

        # everything else must be a diagonal line:
        elif draw_diagonal:
            if x1 > x2:
                # ensure x increases from x1 to x2
                x1, y1, x2, y2 = line[2], line[3], line[0], line[1]

            while x1 <= x2:
                graph[y1][x1] += 1

                x1 += 1
                if y1 < y2: # downhill slope
                    y1 += 1
                else: # uphill slope
                    y1 -= 1

    # count the number of crossing lines
    crossing_lines = 0
    for y in graph:
        for spot in graph[y]:
            if spot > 1:
                crossing_lines += 1
 
    return crossing_lines


def alternate_solution(lines, draw_diagonal=False):
    """
    Inspired by a few solutions I saw - instead of a graph, just use a dict with coordinates as keys
    Also, splice in the crossed line counting to avoid a final sweep through the dict at the end
    This solution should be faster, but harder to troubleshoot, as you cannot just print out the graph
    """
    from collections import defaultdict
    graph = defaultdict(int)

    crossing_lines = 0

    # add coordinates to the "graph":
    for line in lines:
        x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
 
        # vertical line:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                graph[(i, x1)] += 1
                if graph[(i, x1)] == 2:
                    crossing_lines += 1

        # horizontal line:
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                graph[(y1, i)] += 1
                if graph[(y1, i)] == 2:
                    crossing_lines += 1

        # everything else must be a diagonal line:
        elif draw_diagonal:
            if x1 > x2:
                # ensure x increases from x1 to x2
                x1, y1, x2, y2 = line[2], line[3], line[0], line[1]

            while x1 <= x2:
                graph[(y1, x1)] += 1
                if graph[(y1, x1)] == 2:
                    crossing_lines += 1

                x1 += 1
                if y1 < y2:
                    y1 += 1
                else:
                    y1 -= 1

    return crossing_lines


if __name__ == '__main__':
    data = load_data()
    print(f"Data: {data}\n")

    print(f"Part 1: {part1_and_2(data)}")
    print(f"Part 2: {part1_and_2(data, draw_diagonal=True)}\n")
    print(f"Alernate Solution: {alternate_solution(data, draw_diagonal=True)}\n")
