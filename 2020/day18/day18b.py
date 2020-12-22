"""
day18b - https://adventofcode.com/2020/day/18

--- Day 18: Operation Order ---

* Part 2

Now, addition and multiplication have different precedence levels, 
 but they're not the ones you're familiar with.
Instead, addition is evaluated before multiplication.

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
    # recursively pull off layers of parens until we have a numbers and operands only problem
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


    # now that we have removed all the parens, we can evaluate
    answer = evaluate_addition(clean_prob)
    return answer


def evaluate_addition(prob):
    # evaluate a problem that has had all parentheses removed
    # do all addition from left to right - this will be recursively called until there is no addition left
    print(f"add  {prob}")

    if "+" in prob:
        for i in range(len(prob)):
            if prob[i] == "+":
                probsum = int(prob[i-1]) + int(prob[i+1])

                if i >= 1:
                    before = prob[:i-1]
                else:
                    before = []

                if i < len(prob) - 2:
                    after = prob[i+2:]
                else:
                    after = []

                # stitch together a new problem statement
                new_prob = before + [probsum] + after
                break
        return evaluate_addition(new_prob)

    return evaluate_multiplication(prob)


def evaluate_multiplication(prob):
    # now that all addition has been calculated, do all the multiplication from left to right
    # in retrospect, I could probably reuse the recursive addition logic, but it's faster to copy/paste from part1
    print(f"mult {prob}")

    answer = 0
    operand = "+"
    for x in prob:
        # if operand, store it
        if x == "*":
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

    #print(f"{prob} = {answer}")
    return answer


if __name__ == '__main__':
    data = load_data()
    print(f"data: {data} \n")

    results2 = part2(data)
    print(f"\nPart 2 - {results2}")
