# base case is the way out
# forward progress
# recursive progress

def countdown(firstNum):
    if firstNum <=0:
        print("PLease give me a positive number to count down from")
    for i in range(firstNum, 0, -1):
        print(i)

countdown(10)

def recursiveCountdown(firstNum):
    if firstNum <= 0: #basecase
        return 1
    print(firstNum) 
    return recursiveCountdown(firstNum - 1) #forward progress

recursiveCountdown(10)

## Write a function that will return the sum of all numbers from zero up to a given integer

def sumNumbers(givenInteger):
        sumTotal = 0
        for i in range(0, givenInteger+1, 1):
            sumTotal += i
        return sumTotal

print(sumNumbers(4))

def recursiveSum(givenInteger):
    if givenInteger <= 0:
        return 0
    return givenInteger + recursiveSum(givenInteger -1)

print(recursiveSum(5))

# recursiveSum(5) -> Still open the whole time!
# 5 + recursiveSum(4) -> open until 3 and lower call stacks close
# 5 + 4 + recursiveSum(3) -> open until 2 and lower call stacks close
# 5 + 4 + 3 + recursiveSum(2)
# 5 + 4 + 3 + 2 + recursiveSum(1)
# 5 + 4 + 3 + 2 + 1 + recursiveSum(0)
# 5 + 4 + 3 + 2 + 1 + 0
# Print(15)

# 1   2   3   4   5   6
# 1 + 1 + 2 + 3 + 5 + 8

#Write a function that returns the value of the position of the fibinacci sequence

def recursiveFib(positionInt):
    if positionInt == 2 or positionInt == 1:
        return 1
    return recursiveFib(positionInt - 2) + recursiveFib(positionInt - 1) 
    
print(recursiveFib(9))
