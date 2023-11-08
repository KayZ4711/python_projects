#########################################################################################################

# 1. Create a greeting.
# 2. Create your wordlist 
# 3. Randomly choose a word from the list you have created 
# 4. Ask the user to guess a letter
# 5. Bonus: make the program take the input from the user and make it lowercase
# 6. check if the letter is in the word

import random 

print("Welcome to Hangman!")

print("---------------------------------")

words = ["hacker", "bounty", "random", "amazing"]

# Create an empty list
# For each letter in the secret_word add a "_" that will be printed to the console
# Example if the word is Hacker "_", "_", "_", "_", "_", "_"

# Create a variable as an "int" starting at 0 and when it gets to the the number 9 the game ends. 
# Add a print statement telling the user they get 5 guesses. 

secret_word = random.choice(words)
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)
print("---------------------------------")
print("You get 9 Guesses, good luck.")

# Loop through each of the letters in the chosen word 
# If the letter is in the word, replace the "_" with the letter 
# It should look like this: "_", "a", "c", "_", "_", "r"

# Afterwards, use a while loop so the game keeps going, until the word has been guessed. 
num = 0 
game_over = False 

while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter

    if guess not in secret_word:
        num += 1
        guesses_left = num - 9
        print(f"You have {guesses_left} guesses left!")
        if num >= 9:
            print("You loser!")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win!")
        game_over = True