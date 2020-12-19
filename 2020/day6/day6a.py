"""
day6a - https://adventofcode.com/2020/day/6

* Part 1

For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?
7283

"""

def load_data():
    answers = {}
    answer_id = 1
    answers[1] = ""

    datafile = 'input-day6'
    with open(datafile, 'r') as input:
        for line in input:
            cleanline = line.strip()
            # if it's an empty line, move on to the next answer
            if cleanline == "":
                answer_id += 1
                answers[answer_id] = ""
            # otherwise, concatenate the string onto the current answer
            else:
                answers[answer_id] = answers[answer_id] + cleanline

    return answers


def process_data(answers):
    total = 0
    for answer in answers:
        total += len(set(answers[answer]))
    return total


if __name__ == '__main__':
    data = load_data()
    print(data)

    results = process_data(data)
    print(results)
