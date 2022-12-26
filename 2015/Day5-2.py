# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?



def is_string_nice(input_string):
    is_nice = False

    # Contains at least two equal pairs of letters without overlap
    first_condition = False

    # Contains at least one repeating letter with one letter in between
    second_condition = False

    # If both conditions are true the string is "nice"
    if first_condition and second_condition:
        is_nice = True

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