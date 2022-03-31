# --- Day 2: I Was Told There Would Be No Math ---

# The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

# For example:

#     A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
#     A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

# --- Part Two ---

# The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

# For example:

#     A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
#     A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

# How many total feet of ribbon should they order?


input_list = []
total_sq_feet = 0
total_feet_ribbon = 0

# Strips newline characters from input and also creates sublist with the dimensions separated
for item in open('input/Day2.txt'):
    input_list.append(item.strip('\n').split('x'))

for dimensions in input_list:
    # Convert string numbers into integers
    converted_dimensions = [int(dimension) for dimension in dimensions]

    # Dimensions specified
    length = converted_dimensions[0]
    width = converted_dimensions[1]
    height = converted_dimensions[2]

    # Finds total area of present
    present_area = 2 * length * width + 2 * width * height + 2 * height * length

    # Adds the smallest dimension as 'slack' per instructinons
    present_sq_feet = present_area + min([length * width, width * height, height * length])

    # Adds the sq feet to total
    total_sq_feet += present_sq_feet

    # Finds feet of ribbon for wrapping
    largest_dimension = max(converted_dimensions)
    converted_dimensions.remove(largest_dimension)
    feet_ribbon_wrapping = sum(num + num for num in converted_dimensions)
    print(converted_dimensions, feet_ribbon_wrapping)

    # Finds feet of ribbon for bow
    feet_ribbon_bow = length * width * height

    # Adds feet of ribbon to total
    total_feet_ribbon += feet_ribbon_wrapping + feet_ribbon_bow

    
print(f'The elves need to order {total_sq_feet} feet of wrapping paper and {total_feet_ribbon} feet of ribbon.')