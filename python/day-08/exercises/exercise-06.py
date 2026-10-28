"""
Exercise 6 — Character frequency
Ask the user for a sentence and use a dictionary to count the occurrences of each character, ignoring spaces and capitalization.
Challenge: display only characters that occur more than once.
"""

# Get user input
sentence = input("Please enter a sentence: ")

# Count character frequencies
char_count = {}
for char in sentence:
    if char != " ":
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1

# Display characters that occur more than once
print("Characters that occur more than once:")
for char, count in char_count.items():
    if count > 1:
        print(f"'{char}': {count}")