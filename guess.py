"""
Programmer: Ryan Lee

A straightforward number guessing game. Set the max value of the range and then try to find the number in the lease number of guesses!
"""
import random

max = 0
answer = int(input("Number: "))
target = random.randint(0, answer)
# Recalibrate answer so it cannot automatically guess the target
answer += 1
while answer != target:
    answer = int(input("Guess: "))
    if answer > target:
        print("Lower")
    elif answer < target:
        print("Higher")
    else:
        print("Correct! You win!")
