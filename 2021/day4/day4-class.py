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
    #datafile = 'input-day4-example-numbers'
    datafile = 'input-day4-numbers'
    with open(datafile, 'r') as input:
        for line in input:
            numbers = line.strip().split(",")

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

    return numbers, boards


class Bingo():
    def __init__(self, numbers, boards):
        self.numbers = numbers
        self.boards = boards

    def play_p1(self):
        """
        Let's play bingo - figure out which is the *first* winning board

        If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
        Score of the winning board = sum of all unmarked numbers * the number that was just called when the board won
        """
        for number in self.numbers:
            # mark the number on all boards
            for board in self.boards:
                for line_num, line in enumerate(self.boards[board]):
                    for spot_num, spot in enumerate(line):
                        if spot == number:
                            self.boards[board][line_num][spot_num] = "X"

            # check for a winner
            found_winner, winning_board = self.check_for_winning_board()

            # if the first winning board has been found, calculate the score
            if found_winner:
                print(f"Found the first winning board with number {number}")
                pprint(winning_board)
                return self.calculate_score(winning_board, number)

    def play_p2(self):
        """
        Let's play bingo - figure out which is the *last* winning board
        """
        for number in self.numbers:
            # mark the number on all boards
            for board in self.boards:
                for line_num, line in enumerate(self.boards[board]):
                    for spot_num, spot in enumerate(line):
                        if spot == number:
                            self.boards[board][line_num][spot_num] = "X"

            # check for a winner
            found_winner, winning_board = self.check_for_winning_board()

            # if the last winning board has been found, calculate the score
            if found_winner and len(self.boards) == 1:
                print(f"Found the last winning board with number {number}")
                pprint(winning_board)
                return self.calculate_score(winning_board, number)
            # otherwise, remove all winning boards and continue playing
            elif found_winner:
                self.prune_winning_boards()


    def check_for_winning_board(self):
        for board in self.boards:
            columns = [[] for i in range(5)]
            for line in self.boards[board]:
                if len(set(line)) == 1:
                    return True, self.boards[board]

                for spot_num, spot in enumerate(line):
                    columns[spot_num].append(spot)

            for column in columns:
                if len(set(column)) == 1:
                    return True, self.boards[board]

        return False, None

    def calculate_score(self, winning_board, number):
        sum = 0
        for line in winning_board:
            for spot in line:
                if spot != "X":
                    sum += int(spot)

        return sum * int(number)

    def prune_winning_boards(self):
        pruned_boards = deepcopy(self.boards)
        for board in self.boards:
            found_winner = False
            columns = [[] for i in range(5)]
            for line in self.boards[board]:
                if set(line) == {"X"}:
                    found_winner = True

                for spot_num, spot in enumerate(line):
                    columns[spot_num].append(spot)

            for column in columns:
                if set(column) == {"X"}:
                    found_winner = True

            if found_winner:
                pruned_boards.pop(board)

        self.boards = pruned_boards


if __name__ == '__main__':
    numbers, boards = load_data()
    print(f"Numbers: {numbers}\n")
    print(f"Bingo boards: {boards}\n")

    print(f"Part 1: {Bingo(numbers, boards).play_p1()}")
    print(f"Part 2: {Bingo(numbers, boards).play_p2()}\n")
