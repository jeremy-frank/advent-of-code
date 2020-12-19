"""
day6b - https://adventofcode.com/2020/day/6

* Part 2

Example: 6

Identify the questions to which everyone answered "yes"!
3520

"""
def load_data():
    answers = {}
    answer_id = 1
    answers[1] = []

    datafile = 'input-day6'
    with open(datafile, 'r') as input:
        for line in input:
            cleanline = line.strip()
            # if it's an empty line, move on to the next answer
            if cleanline == "":
                answer_id += 1
                answers[answer_id] = []
            # otherwise, append the answer to the current answer
            else:
                answers[answer_id].append(cleanline)

    return answers


def process_data(answers):
    total = 0
    for answer_id in answers:
        answer_list = answers[answer_id]
        alphabet = {}
        for answer in answer_list:
            for char in answer:
                # really should use defaultdict instead
                if char not in alphabet:
                    alphabet[char] = 0
                alphabet[char] += 1
        for letter in alphabet:
            quantity = alphabet[letter]
            if quantity == len(answer_list):
                total += 1
    return total


if __name__ == '__main__':
    data = load_data()
    print(data)

    results = process_data(data)
    print(results)
