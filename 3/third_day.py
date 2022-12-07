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

def getBadgeWithList(rucksackList):
    return getBadge(rucksackList[0], rucksackList[1], rucksackList[2])

def getBadge(firstRucksack, secondRucksack, thirdRucksack):
    badge = ''.join(set(firstRucksack).intersection(secondRucksack).intersection(thirdRucksack))
    return badge

def getAnswerPartOne():
    initializePriorities()

    f = open("3/input_part_1.txt")
    lines = f.readlines()

    sum = 0

    for line in lines:
        # Get the common letter of the current line
        commonLetter = getCommonLetter(line)

        print(f'Common: {commonLetter}')

        # Add the common letter value to the total sum
        sum += values[commonLetter]

    # Close the reader
    f.close()

    print(f'Total priority: {sum}')

def getAnswerPartTwo():
    initializePriorities()

    f = open("3/input_part_1.txt")
    lines = f.readlines()

    sum = 0
    index = 0
    rucksackList = []

    for line in lines:
        # Add one to the current index
        index += 1

        if index % 3 == 0:
            # Remove the new line operator
            rucksackList.append(line.replace('\n', ''))

            badge = getBadgeWithList(rucksackList)

            sum += values[badge]
            rucksackList.clear()
        else:
            rucksackList.append(line)

    print(f'Answer part 2: {sum}')

getAnswerPartTwo()