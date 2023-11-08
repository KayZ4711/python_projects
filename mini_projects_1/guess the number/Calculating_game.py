# Import the random and time modules, which provide functions for random number generation and time operations, respectively.
import random
import time 

# A list of string operators for mathematical operations.
OPERATORS = ["+", "-", "*"]

# Constants defining the range of operands (numbers) to be used in problems.
MIN_OPERAND = 3
MAX_OPERAND = 12

# The total number of problems to be generated and solved by the user.
TOTAL_PROBLEMS = 10 

# This function generates a single math problem using random operands and an operator.
def generate_problem(): 
    # Choose a random number for the left operand within the specified range.
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    # Choose a random number for the right operand within the specified range.
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    # Randomly select an operator from the list of operators.
    operator = random.choice(OPERATORS)

    # Construct the math problem as a string.
    expr = str(left) + " " + operator + " " + str(right) 
    # Calculate the answer by evaluating the expression string.
    answer = eval(expr)
    # Return the problem and its answer.
    return expr, answer

# Initialize a counter for the number of wrong answers.
wrong = 0

# Wait for the user to press enter to start the game.
input("Press enter to start!")
print("----------------------------")  # Print a separator line.

# Record the start time of the game.
start_time = time.time() 

# Loop TOTAL_PROBLEMS times to generate and ask math problems.
for i in range(TOTAL_PROBLEMS):
    # Generate a new problem.
    expr, answer = generate_problem()
    while True:
        # Prompt the user for their answer to the problem.
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ") 
        # Check if the user's guess is correct.
        if guess == str(answer):
            # If correct, exit the loop and move to the next problem.
            break
        # If the guess is wrong, increment the wrong answer counter.
        wrong += 1

# Record the end time of the game.
end_time = time.time()
# Calculate the total time taken by subtracting the start time from the end time.
total_time = end_time - start_time 

# Print another separator line.
print("----------------------------")
# Congratulate the user and display the time taken to finish the game.
print("Nice work! You finished in", total_time, "seconds!")
