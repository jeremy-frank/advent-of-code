"""
day18b - https://adventofcode.com/2020/day/18

--- Day 18: Operation Order ---

* Part 2

Addition is evaluated before multiplication.

Examples:
1 + 2 * 3 + 4 * 5 + 6 becomes 231
1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

What do you get if you add up the results of evaluating the homework problems using these new rules?
70518821989947

"""
def load_data():
    data = []
    datafile = 'input-day18'
    #datafile = 'input-day18-example'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())
    return data


def part2(data):
    answers = []
    for prob in data:
        print("---------------------")
        print(f"problem: {prob}")
        answers.append(unwind_parens(prob.split()))
    print(f"\nanswers: {answers}")
    return sum(answers)


def unwind_parens(prob):
    # recursively pull off layers of parens until we have a numbers and operators only problem
    clean_prob = []
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
                    paren_answer = unwind_parens(paren_prob)
                    clean_prob.append(paren_answer)
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

        else:
            clean_prob.append(x)


    # now that we have removed all the parens, we can evaluate the operators
    mult_only_prob = evaluate_operator(clean_prob, "+")
    answer = evaluate_operator(mult_only_prob, "*")
    return answer[0]


def evaluate_operator(prob, op):
    # evaluate a problem that has had all parentheses removed
    # perform either + or * from left to right - this will be recursively called until there are no instances of that operator
    print(f"{op} {prob}")

    if op in prob:
        for i in range(len(prob)):
            if prob[i] == op:

                if prob[i] == "+":
                    result = int(prob[i-1]) + int(prob[i+1])
                elif prob[i] == "*":
                    result = int(prob[i-1]) * int(prob[i+1])

                # stitch together a new problem statement
                new_prob = prob[:i-1] + [result] + prob[i+2:]
                break
        return evaluate_operator(new_prob, op)

    return prob


if __name__ == '__main__':
    data = load_data()
    print(f"data: {data} \n")

    results2 = part2(data)
    print(f"\nPart 2 - {results2}")
