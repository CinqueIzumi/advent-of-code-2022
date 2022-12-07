import re

def getAnswerPartOne():
    f = open("4/input_part_1.txt")
    lines = f.readlines()

    total = 0

    for line in lines:
        # Split the values in an in array
        values = [int(number) for number in re.findall(r'\d+', line)]

        # Assign the int array's values to their respective variables
        firstStart = values[0]
        firstEnd = values[1]
        secondStart = values[2]
        secondEnd = values[3]

        # Check if the second elf's areas are contained within the first elf's areas
        if firstStart <= secondStart and firstEnd >= secondEnd:
            total += 1
        # Check if the first elf's areas are contained within the second elf's areas
        elif secondStart <= firstStart and secondEnd >= firstEnd:
            total += 1

    f.close()

    print(f'overlaps: {total}')

getAnswerPartOne()