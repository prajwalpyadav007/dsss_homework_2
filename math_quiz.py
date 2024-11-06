import random


def generate_integers(min_value, max_value):
    """
    Generates a integer in the given range.
    parameters: 
        min_value: minimum value of the range
        max_value: maximum value of the range
    
    Returns:
        random integer from the diven range

    """
    return random.randint(min_value, max_value)


def generate_operator():
    """
    random selection of operator
    returns:
        A random operator, either '+', '-', '*'
    """
    return random.choice(['+', '-', '*'])


def generate_problem(num_1, num_2, operator):
    """
    generate math problem and calculate answer
    Parameter:
        num_1:first value in the math problem
        num_2:second value in the math problem
        operator: the operator'+', '-', '*'
    returns:
        the problem and the correct answer
    """
    problem = f"{num_1} {operator} {num_2}"
    if operator == '+':
        answer = num_1 + num_2
    elif operator == '-': 
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3 #number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num_1 = generate_integers(1, 10)
        num_2 = generate_integers(1, 5)
        operator = generate_operator()

        problem, correct_answer = generate_problem(num_1, num_2, operator)
        print(f"\nQuestion: {problem}")

        try:
            useranswer = int(input("Your answer: "))
            if useranswer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print(f"Invalid input. Please enter an integer")
    print(f"\nGame over! Your score is: {score}/{total_questions}")
if __name__ == "__main__":
    math_quiz()

