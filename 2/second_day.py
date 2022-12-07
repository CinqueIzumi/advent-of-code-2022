from enum import Enum

class Symbol(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

# Function which can be used to calculate a match's score, based on the user's and opponent's choices
def calculateScore(opp, user):
    score = 0
    # Add the value of the symbol to the score
    score += user.value

    # Add a draw to the score
    if user.value == opp.value:
        score += 3
    
    # If the user won, add 6 to the score
    elif user == Symbol.ROCK:
        if opp == Symbol.SCISSOR:
            score += 6
    elif user == Symbol.PAPER:
        if opp == Symbol.ROCK:
            score += 6
    elif user == Symbol.SCISSOR:
        if opp == Symbol.PAPER:
            score += 6
    
    return score

# Parse a string input to a symbol enum
def parseInput(input):
    if input == 'A' or input == 'X':
        return Symbol.ROCK

    if input == 'B' or input == 'Y':
        return Symbol.PAPER

    if input == 'C' or input == 'Z':
        return Symbol.SCISSOR

# A function which can be used to get a losing matchup, based on the opponents choice
def getLosingMatchup(opp):
    match opp:
        case Symbol.ROCK:
            return Symbol.SCISSOR
        case Symbol.PAPER:
            return Symbol.ROCK
        case Symbol.SCISSOR:
            return Symbol.PAPER

# A function which can be used to get a winning matchup, based on the opponents choice
def getWinningMatchup(opp):
    match opp:
        case Symbol.ROCK:
            return Symbol.PAPER
        case Symbol.PAPER:
            return Symbol.SCISSOR
        case Symbol.SCISSOR:
            return Symbol.ROCK

# Calculate which choice should be used, based on opponent choice and the required result
def calculateChoice(opp, result): 
    if result == 'X':
        return getLosingMatchup(opp)
    elif result == 'Y':
        return opp
    elif result == 'Z':
        return getWinningMatchup(opp)

def firstAnswer():
    f = open("2/input.txt")
    lines = f.readlines()

    userScore = 0
    for line in lines:
        # First character in string is opponent value, Third (space counts as character) is user value
        oppValue = line[0]
        userValue = line[2]

        # Add the score to the total user's score
        userScore += calculateScore(parseInput(oppValue), parseInput(userValue))

    print(f'User score: {userScore}')

    # Close the file
    f.close()

def secondAnswer():
    f = open("2/input.txt")
    lines = f.readlines()

    userScore = 0
    for line in lines:
        # First character in string is opponent value, Third (space counts as character) is user value
        oppValue = line[0]
        userValue = line[2]

        opponentChoice = parseInput(oppValue)

        # Add the score to the total user's score
        userScore += calculateScore(opponentChoice, calculateChoice(opponentChoice, userValue))

    print(f'User score: {userScore}')

    # Close the file
    f.close()


firstAnswer()
secondAnswer()