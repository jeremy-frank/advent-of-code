"""
day18a - https://adventofcode.com/2020/day/18

--- Day 18: Operation Order ---

* Part 1

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), 
 and parentheses ((...)).

The rules of operator precedence have changed.
Rather than evaluating multiplication before addition, 
  the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

Example answers:
71
51
26
437
12240
13632

Evaluate the expression on each line of the homework; what is the sum of the resulting values?
5019432542701

"""
def load_data():
    data = []
    datafile = 'input-day18'
    #datafile = 'input-day18-example'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())
    return data


def part1(data):
    answers = []
    for prob in data:
        answers.append(evaluate_problem(prob.split()))

    print(f"answers: {answers}")
    return sum(answers)


def evaluate_problem(prob):
    answer = 0

    operand = "+"
    parens = False
    for x in prob:
        
        if parens == True:
            if x[0] == "(":
                for char in x:
                    if char == "(":
                        open_paren_count += 1
                paren_prob.append(x)
            elif x[-1] == ")":
                for char in x:
                    if char == ")":
                        close_paren_count += 1

                if open_paren_count == close_paren_count:
                    paren_prob.append(x[:-1])

                    # recursively call evaluate_problem with just the parentheses part of the problem
                    paren_answer = evaluate_problem(paren_prob)

                    if operand == "+":
                        answer += paren_answer
                    elif operand == "*":
                        answer *= paren_answer
                    parens = False
                else:
                    paren_prob.append(x)
            else:
                paren_prob.append(x)

        elif x[0] == "(":
            parens = True
            open_paren_count = 0
            close_paren_count = 0
            for char in x:
                if char == "(":
                    open_paren_count += 1
            paren_prob = [x[1:]]

        # if operand, store it
        elif x in ["+", "*"]:
            operand = x

        # if number, apply operand
        else:
            num = int(x)
            if operand == "+":
                answer += num
            elif operand == "*":
                answer *= num
            else:
                print("Error!")

    print(f"{prob} = {answer}")
    return answer


if __name__ == '__main__':
    data = load_data()
    print(f"data: {data} \n")

    results1 = part1(data)
    print(f"\nPart 1 - {results1}")
