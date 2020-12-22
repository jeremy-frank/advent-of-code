"""
day22ab - https://adventofcode.com/2020/day/22

--- Day 22: Crab Combat ---

* Part 1
Play Combat
Each player has their own deck (input)

The game consists of a series of rounds:
- both players draw their top card
- the player with the higher-valued card wins the round.
- The winner keeps both cards, placing them on the bottom of 
  their own deck so that the winner's card is above the other card.  
- If this causes a player to have all of the cards, they win, and the game ends

Calculate the winning player's score
The bottom card in their deck is worth the value of the card multiplied by 1, 
  the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on

Example: 306

Play the small crab in a game of Combat using the two decks you just dealt.
What is the winning player's score?
32413


* Part 2
Challenge the small crab to a game of Recursive Combat
Same starting decks as before
Use same scoring rules from Part1

- Before either player deals a card, if there was a previous round in this game that had exactly 
  the same cards in the same order in the same players' decks, the game instantly ends in a win 
  for player 1. Previous rounds from other games are not considered. (This prevents infinite games 
  of Recursive Combat, which everyone agrees is a bad idea.)
- Otherwise, this round's cards must be in a new configuration; the players begin the round by each
  drawing the top card of their deck as normal.
- If both players have at least as many cards remaining in their deck as the value of the card they
  just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
- Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner
  of the round is the player with the higher-value card.

Example: 291

Playing the small crab in a game of Recursive Combat using the same two decks as before.
What is the winning player's score?
31596

Notes: Took me a long time to realize I need to deepcopy deck1/deck2 when I add them to history1/history2
Runtime: About 9s
"""
import copy

def load_decks():
    deck1 = []
    #datafile = 'input-day22-player1-example'
    datafile = 'input-day22-player1'
    with open(datafile, 'r') as input:
        for line in input:
            deck1.append(int(line.strip()))

    deck2 = []
    #datafile = 'input-day22-player2-example'
    datafile = 'input-day22-player2'
    with open(datafile, 'r') as input:
        for line in input:
            deck2.append(int(line.strip()))

    return deck1, deck2


def part1(deck1, deck2):
    print("Would you like to play a game?")

    winner = False
    while not winner:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
        
        if not deck1:
            winner = True
            winning_deck = deck2
        if not deck2:
            winner = True
            winning_deck = deck1

    score = 0
    deck_size = len(winning_deck)
    for card in winning_deck:
        score += card * deck_size
        deck_size -= 1

    return score


def part2(deck1, deck2):
    history1 = []
    history2 = []

    #print("---------------------")
    #print(f"starting game with deck1 {deck1}, deck2 {deck2}")

    while True:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 <= len(deck1) and card2 <= len(deck2):
            winner, _ = part2(deck1[:card1], deck2[:card2])
        elif card1 > card2:
            #print(f"{card1} > {card2} - deck1 {deck1}, deck2 {deck2}")
            winner = 1
        else:
            #print(f"{card1} < {card2} - deck1 {deck1}, deck2 {deck2}")
            winner = 2


        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)


        if not deck1:
            #print(f"Winner 2 - deck 1 {deck1}, deck2 {deck2}")
            return 2, score_deck(deck2)

        elif not deck2:
            #print(f"Winner 1 - deck 1 {deck1}, deck2 {deck2}")
            return 1, score_deck(deck1)

        elif (deck1 in history1) and (deck2 in history2):
            # infinite loop found, immediate win for player1
            #print(f"Deck match - deck1 {deck1}, deck2 {deck2}")
            return 1, score_deck(deck1)

        else:
            history1.append(copy.deepcopy(deck1))
            history2.append(copy.deepcopy(deck2))


def score_deck(deck):
    score = 0
    deck_size = len(deck)
    for card in deck:
        score += card * deck_size
        deck_size -= 1

    return score


if __name__ == '__main__':
    deck1, deck2 = load_decks()
    print(f"deck1: {deck1}")
    print(f"deck2: {deck2} \n")

    results1 = part1(copy.deepcopy(deck1), copy.deepcopy(deck2))
    print(f"\nPart 1 - {results1}")

    winner, score = part2(copy.deepcopy(deck1), copy.deepcopy(deck2))
    print(f"Part 2 - {score}")
