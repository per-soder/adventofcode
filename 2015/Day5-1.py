# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?



# Define vowels
VOWELS = ['a', 'e', 'i', 'o', 'u']

# Define "forbidden" strings
FORBIDDEN_STRINGS = ['ab', 'cd', 'pq', 'xy']

# Function for deciding if string is "nice"
def is_string_nice(input_string):
    is_nice = False

    # Find amount of vowels in string
    vowels_amount = 0

    for letter in input_string:
        if letter in VOWELS:
            vowels_amount += 1

    # Check if string contains a letter that appears twice in a row
    has_consecutive_letters = False

    for index, char in enumerate(input_string):
        # Skip if first letter in loop
        if index == 0:
            continue

        previous_char = input_string[index - 1]

        # If current char equals previous char return true and break loop
        if previous_char == char:
            has_consecutive_letters = True
            break
    
    # Check if string contains at least three vowels and has consecutive letters
    if vowels_amount >= 3 and has_consecutive_letters:
        is_nice = True
    
    # Check that string does not contain "forbidden" string as substring 
    for forbidden_string in FORBIDDEN_STRINGS:
        if forbidden_string in input_string:
            is_nice = False

    return is_nice

# Get strings from file
file_strings = []

with open('input/Day5.txt') as input_file:
    for strings in input_file:
        file_strings.append(strings.rstrip())

# Decide which strings are "nice"
nice_strings = []

for string in file_strings:
    if is_string_nice(string):
        nice_strings.append(string)

print(f"Amount of 'nice' strings: {len(nice_strings)}")