# Open the file named 'story.txt' in read mode. This is a context manager that automatically
# closes the file when the block of code is done executing.
with open("story.txt", "r") as f:
    story = f.read()  # Read the entire contents of the file and store it in the variable 'story'.

# Initialize an empty set called 'words'. Sets are like lists but can only contain unique elements.
words = set()

# We'll use 'start_of_word' to remember the position where a special word starts. Initialize it to -1 to indicate that we are not currently tracking a word.
start_of_word = -1

# Define the start and end markers for the words we want to capture.
target_start = "<"
target_end = ">"

# Iterate over 'story', with both the index (i) and the character (char) at that index.
for i, char in enumerate(story):
    if char == target_start:  # If the character is the start marker...
        start_of_word = i  # ... remember the index where this word starts.

    # If the character is the end marker and we have a valid start index...
    if char == target_end and start_of_word != -1:
        # Slice the story from the start marker to the end marker (inclusive) to get the word.
        word = story[start_of_word: i + 1]
        words.add(word)  # Add the captured word to the 'words' set.
        start_of_word = -1  # Reset 'start_of_word' as we've finished capturing this word.

# Initialize a dictionary called 'answers' where we will map words to user-provided replacements.
answers = {}

# Iterate over the unique words we found in the story.
for word in words:
    # Prompt the user to enter a replacement for the current word and store the input in 'answer'.
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer  # Map the original word to the user's answer in the 'answers' dictionary.

# Iterate over the words again.
for word in words:
    # Replace all instances of the current word in 'story' with the user's answer.
    story = story.replace(word, answers[word])

# Finally, print the set of words that we found and replaced.
# This will show the unique words that were enclosed in the target markers.
print(words)
