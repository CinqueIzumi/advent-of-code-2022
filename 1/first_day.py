f = open("1/input.txt")
lines = f.readlines()

total = 0
numbers = []

for value in lines:
    if value == '\n':
        # If there's a line break, add the total to the number array
        numbers.append(total)

        # Reset the total as a new elf will start
        total = 0
    else:
        total = total + int(value)

# Sort the numbers based on ascending order
numbers.sort(reverse=True)
print(f'Highest: {numbers[0]}')

topThree = numbers[0] + numbers[1] + numbers[2]
print(f'Top 3: {topThree}')

# Close the file
f.close()