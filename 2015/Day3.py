# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

#     > delivers presents to 2 houses: one at the starting location, and one to the east.
#     ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#     ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.



# Input text file made into list of characters
input_list = []

with open('input/Day3.txt') as input_file:
    for directions in input_file:
        input_list = [char for char in directions]

# Storing result
houses_visited = 1

# Record Santas current position
northward = 0
eastward = 0

# Store all positions for comparing
locations_list = [[0, 0]]

for direction in input_list:
    if direction == '^':
        northward += 1
    elif direction == 'v':
        northward -= 1
    elif direction == '<':
        eastward -= 1
    elif direction == '>':
        eastward += 1
    else:
        None

    # Check if position has already been visited, add to houses_visited if it hasn't
    current_position = [northward, eastward]

    if current_position not in locations_list:
        locations_list.append(current_position)
        houses_visited += 1

print(f'{houses_visited} houses received at least one present.')

# --- Part Two ---

# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

#     ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.



# Storing result
houses_visited_second_year = 1

# Record Santas and Robo-Santa current positions
santa_position = {
    "north": 0,
    "east": 0
}

robot_santa_position = {
    "north": 0,
    "east": 0
}

# Store all positions for comparing
combined_locations_list = [[0, 0]]

# Decide which moves are to be made
for index, direction in enumerate(input_list):
    if direction == '^':
        if index % 2 == 0:
            robot_santa_position["north"] += 1
        else:
            santa_position["north"] += 1
    elif direction == 'v':
        if index % 2 == 0:
            robot_santa_position["north"] -= 1
        else:
            santa_position["north"] -= 1
    elif direction == '>':
        if index % 2 == 0:
            robot_santa_position["east"] += 1
        else:
            santa_position["east"] += 1
    elif direction == '<':
        if index % 2 == 0:
            robot_santa_position["east"] -= 1
        else:
            santa_position["east"] -= 1
    else:
        None

    # Check if position has already been visited, add to houses_visited if it hasn't
    current_position_second_year = [robot_santa_position["north"], robot_santa_position["east"]] if index % 2 == 0 else [santa_position["north"], santa_position["east"]]

    if current_position_second_year not in combined_locations_list:
        combined_locations_list.append(current_position_second_year)
        houses_visited_second_year += 1

print(f'{houses_visited_second_year} houses received at least one present on the next year.')