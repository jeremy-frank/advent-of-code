"""
--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10

summary: track open/close brackets

"""
from copy import deepcopy

def load_data():
    #datafile = 'input-day10-example'
    datafile = 'input-day10'
    data = []
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())
    return data


def part1(data):
    """
    The navigation subsystem syntax is made of several lines containing chunks.
    There are one or more chunks on each line, and chunks contain zero or more other chunks.

    Every chunk must open and close with one of four legal pairs of matching characters:
    If a chunk opens with (, it must close with ).
    If a chunk opens with [, it must close with ].
    If a chunk opens with {, it must close with }.
    If a chunk opens with <, it must close with >.

    Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.
    A corrupted line is one where a chunk closes with the wrong character

    To calculate the syntax error score for a line, take the first illegal character on the line:
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.

    What is the total syntax error score for those errors?
    """
    syntax_error_score = 0

    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    char_check = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    for line in data:
        found_illegal_char = False
        active_chunks = []
        for char in line:
            if not found_illegal_char:
                if char in ["(", "[", "{", "<"]:
                    active_chunks.append(char)
                else:
                    if char == char_check[active_chunks[-1]]:
                        active_chunks.pop(-1)
                    else:
                        print(f"Expected close to {active_chunks[-1]} but found {char}")
                        found_illegal_char = True
                        syntax_error_score += points[char]

    return syntax_error_score


def part2(data):
    """
    Incomplete lines don't have any incorrect characters,
    Instead, they're missing some closing characters at the end of the line
    Figure out the sequence of closing characters that complete all open chunks in the line
    You can only use closing characters (), ], }, or >)
    You must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

    Score - start with zero
    Then, for each character:
      multiply the total score by 5
      increase the total score by the point value given for the character in the following table

    ): 1 point.
    ]: 2 points.
    }: 3 points.
    >: 4 points.

    the winner is found by sorting all of the scores and then taking the middle score.
    There will always be an odd number of scores to consider.
    What is the middle score?
    """
    incomplete_scores = []

    char_check = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    for line in data:
        found_illegal_char = False
        active_chunks = []
        for char in line:
            if not found_illegal_char:
                if char in ["(", "[", "{", "<"]:
                    active_chunks.append(char)
                else:
                    if char == char_check[active_chunks[-1]]:
                        active_chunks.pop(-1)
                    else:
                        #print(f"Expected close to {active_chunks[-1]} but found {char}")
                        found_illegal_char = True
                        active_chunks = []

        if active_chunks:
            print(f"Found incomplete line {line}, active chunks {active_chunks}")
            incomplete_scores.append(calculate_incomplete_score(active_chunks))

    incomplete_scores.sort()
    print(f"Incomplete scores: {incomplete_scores}")
    halfway = int(len(incomplete_scores) / 2)
    return incomplete_scores[halfway]


def calculate_incomplete_score(chunks):
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    score = 0
    chunks.reverse()
    for chunk in chunks:
        score = score * 5
        score += points[chunk]
    
    return score


if __name__ == '__main__':
    data = load_data()
    print(f"Data1: {data}\n")
    print(f"Part 1: {part1(deepcopy(data))}\n")
    print(f"Part 2: {part2(deepcopy(data))}\n")
