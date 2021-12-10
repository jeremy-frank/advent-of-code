"""
--- Day 4: Giant Squid ---
https://adventofcode.com/2021/day/4

summary: squid bingo, find first/last winning bingo board

Part 1: 33348
Part 2: 8112
"""
from copy import deepcopy
from pprint import pprint

def load_data():
    #datafile = 'input-day4-example-guesses'
    datafile = 'input-day4-guesses'
    with open(datafile, 'r') as input:
        for line in input:
            guesses = line.strip().split(",")

    #datafile = 'input-day4-example-boards'
    datafile = 'input-day4-boards'
    boards = {}
    board_num = 0
    with open(datafile, 'r') as input:
        for line in input:
            if not line.strip():
                board_num += 1
                boards[board_num] = []
            else:
                board_line = line.strip().split()
                boards[board_num].append(board_line)

    return guesses, boards


def part1(guesses, boards):
    """
    Bingo - find the first board to win
    Numbers are chosen at random, and the chosen number is marked on all boards on which it appears
    If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

    score of the winning board = sum of all unmarked numbers * the number that was just called when the board won
    """
    for guess in guesses:
        for board in boards:
            for line_num, line in enumerate(boards[board]):
                for spot_num, spot in enumerate(line):
                    if spot == guess:
                        boards[board][line_num][spot_num] = "X"

        # check for a winner
        found_winner, winning_board = check_for_winning_board(boards)

        # calculate the score
        if found_winner:
            print(f"Found the first winning board with guess {guess}")
            pprint(winning_board)
            return calculate_score(winning_board, guess)


def part2(guesses, boards):
    """
    Bingo - figure out which board will win last
    """
    for guess in guesses:
        for board in boards:
            for line_num, line in enumerate(boards[board]):
                for spot_num, spot in enumerate(line):
                    if spot == guess:
                        boards[board][line_num][spot_num] = "X"

        # check for a winner
        found_winner, winning_board = check_for_winning_board(boards)

        # calculate the score
        if found_winner and len(boards) == 1:
            print(f"Found the last winning board with guess {guess}")
            pprint(winning_board)
            return calculate_score(winning_board, guess)
        elif found_winner:
            boards = remove_winning_boards(boards)


def check_for_winning_board(boards):
    for board in boards:
        columns = [[] for i in range(5)]
        for line in boards[board]:
            if len(set(line)) == 1:
                return True, boards[board]

            for spot_num, spot in enumerate(line):
                columns[spot_num].append(spot)

        for column in columns:
            if len(set(column)) == 1:
                return True, boards[board]

    return False, None


def calculate_score(winning_board, guess):
    sum = 0
    for line in winning_board:
        for spot in line:
            if spot != "X":
                sum += int(spot)

    return sum * int(guess)


def remove_winning_boards(boards):
    pruned_boards = deepcopy(boards)
    for board in boards:
        found_winner = False
        columns = [[] for i in range(5)]
        for line in boards[board]:
            if set(line) == {"X"}:
                found_winner = True

            for spot_num, spot in enumerate(line):
                columns[spot_num].append(spot)

        for column in columns:
            if set(column) == {"X"}:
                found_winner = True

        if found_winner:
            pruned_boards.pop(board)

    return pruned_boards


if __name__ == '__main__':
    guesses, boards = load_data()
    print(f"Guesses: {guesses}\n")
    print(f"Bingo boards: {boards}\n")
    print(f"Part 1: {part1(guesses, deepcopy(boards))}")
    print(f"Part 2: {part2(guesses, deepcopy(boards))}\n")
