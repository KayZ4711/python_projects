# This code simulates a dice-rolling game where 2 to 4 players roll a die, and the first player to reach or exceed a score of 50 wins. 
# If a player rolls a 1, their turn is over, and they score nothing for that round.

# Importing the random module to generate random numbers
import random

# Defining a function to simulate rolling a dice
def roll():
    min_value = 1  # Setting the minimum value of the dice roll to 1
    max_value = 6  # Setting the maximum value of the dice roll to 6
    roll = random.randint(min_value, max_value)  # Generating a random integer between 1 and 6 (inclusive)

    return roll  # Returning the value of the dice roll

# Infinite loop to ensure the user enters a valid number of players
while True: 
    # Prompting the user to enter the number of players
    players = input("Enter the number of players (2 - 4): ")
    
    # Checking if the entered value is a digit (numeric value)
    if players.isdigit():
        players = int(players)  # Converting the string input to an integer
        
        # Validating if the entered number of players is between 2 and 4
        if 2 <= players <= 4:
            break  # Exiting the loop if a valid number is entered
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")  # Invalid input

# Setting the maximum score required to win the game
max_score = 50

# Initializing the scores of all players to 0
# Using a list comprehension to create a list of zeros with the length equal to the number of players. 
player_scores = [0 for _ in range(players)]

# Game loop: Continue the game until a player reaches the max_score
while max(player_scores) < max_score:
    
    # Looping through each player for their turn
    for player_idx in range(players):
        print("Player number", player_idx + 1, "turn has just started!\n")
        print("Your total score is: ", player_scores[player_idx], "\n")
        
        current_score = 0  # Initializing the current score for the turn
        
        # Player's turn loop
        while True:
            should_roll = input("Would you like to roll (y)? ")
            
            # If the player chooses not to roll, exit the loop
            if should_roll.lower() != "y":
                break

            value = roll()  # Simulating the dice roll
            
            # Checking if the dice roll is a 1
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0  # Resetting the score to 0 if a 1 is rolled
                break
            else:
                current_score += value  # Adding the dice value to the current score
                print("You rolled a: ", value)

            print("Your score is: ", current_score)
    
        # Adding the current score to the player's total score
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

# Identifying the player with the highest score
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
