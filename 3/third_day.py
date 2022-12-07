import string

values = dict()
def initializePriorities():
    # Map a - z with values 1 - 26
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1

    # Map A - Z with values 27 - 52
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 27

def getCommonLetter(input):
    # Calculate where the first compartment ends and the second starts
    compartmentSize = int((len(input) / 2))

    # Initialize the compartment strings
    firstCompartment = input[0:(compartmentSize)]
    secondCompartment = input[compartmentSize:]

    print(f'first: {firstCompartment}, second: {secondCompartment}')

    # Determine what the common letter is
    commonLetter = ''.join(set(firstCompartment).intersection(secondCompartment))
    return commonLetter

initializePriorities()

f = open("3/input.txt")
lines = f.readlines()

sum = 0

for line in lines:
    # Get the common letter of the current line
    commonLetter = getCommonLetter(line)

    # Add the common letter value to the total sum
    sum += values[commonLetter]

# Close the reader
f.close()

print(f'Total priority: {sum}')