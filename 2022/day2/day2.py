"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2

summary: calculate score for win/lose/draw in rock/paper/scissors

Part 1 - 14531
Part 2 - 11258
"""


def load_data():
    datafile = "input-day2"

    data = []
    with open(datafile, "r") as input:
        for line in input:
            vals = line.strip().split(" ")
            data.append(vals)

    return data


def part1(tournament):
    """
    The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors
    The second column must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors

    The winner of the whole tournament is the player with the highest score.
    Your total score is the sum of your scores for each round.
    The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
     plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    What would your total score be if everything goes exactly according to your strategy guide?
    """
    guide = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lose": 0,
        "draw": 3,
        "win": 6,
    }

    total_score = 0
    for round in tournament:
        opp = guide[round[0]]
        me = guide[round[1]]

        # add points for chosen symbol
        total_score += points[me]

        # draw
        if opp == me:
            total_score += points["draw"]
        # win
        elif (
            (opp == "rock" and me == "paper")
            or (opp == "paper" and me == "scissors")
            or (opp == "scissors" and me == "rock")
        ):
            total_score += points["win"]

    return total_score


def part2(tournament):
    """
    Actually, the second column says how the round needs to end:
     X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

    The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
     plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    Following the Elf's instructions for the second column,
    What would your total score be if everything goes exactly according to your strategy guide?
    """
    guide = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "lose": 0,
        "draw": 3,
        "win": 6,
    }

    total_score = 0

    for round in tournament:
        opp = guide[round[0]]
        outcome = guide[round[1]]

        # add points for desired outcome
        total_score += points[outcome]

        if outcome == "draw":
            total_score += points[opp]

        elif outcome == "win":
            if opp == "rock":
                total_score += points["paper"]
            elif opp == "paper":
                total_score += points["scissors"]
            elif opp == "scissors":
                total_score += points["rock"]

        elif outcome == "lose":
            if opp == "rock":
                total_score += points["scissors"]
            elif opp == "paper":
                total_score += points["rock"]
            elif opp == "scissors":
                total_score += points["paper"]

    return total_score


if __name__ == "__main__":
    data = load_data()
    print(f"{data}\n")

    results1 = part1(data)
    print(f"Part 1 - {results1}")

    results2 = part2(data)
    print(f"Part 2 - {results2}\n")
