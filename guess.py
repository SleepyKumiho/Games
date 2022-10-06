"""
Programmer: Ryan Lee

A simple game of guess the number. Players can input the max on the range of possible values, and choose to guess a computer
generated value, or have a CPU guess a number of their choice.
"""

import random
import time

# Game mode where user guesses the hidden number
def user_guess(target):
    guesses = 0
    answer = ""
    while answer != target:
        answer = int(input("Guess: "))
        guesses += 1
        if answer > target:
            print("Lower")
        elif answer < target:
            print("Higher")
        else:
            print("Correct! You win!")
            print(f"You guessed it in {guesses} guesses!")
    return guesses

# Game mode where CPU guesses a number the user chooses
def cpu_guess(target, max):
    guesses = 0
    min = 0
    guess = max + 1
    while guess != target:
        guess = random.randint(min, max)
        print(f"CPU guessed: {guess}")
        guesses += 1
        if guess < target:
            print("Higher")
            min = guess + 1
        elif guess > target:
            print("Lower")
            max = guess - 1
        else:
            print("Correct! CPU wins!")
            print(f"It took the CPU {guesses} guesses!")
            return guesses
        time.sleep(1)

answer = ""
print("Welcome to the guessing game!")
print("To exit at any time, simply type 'quit'")
while answer != "quit":
    max = 0
    print("Please enter a number for the maximum range of possible numbers!")
    while answer != None:
        answer = input("Max: ")
        if answer == "quit":
            print("Come back soon!")
            quit()
        try:
            answer = int(answer)
        except ValueError:
            print("Whoops! Please only enter integers!")
            continue
        break       
        
    max = int(answer)
    target = random.randint(0, answer)
    print("what mode do you wanna play?")
    print("User Guesser or CPU Guesser?")
    answer = input("u/c: ").lower()

    print("Game Starting!")
    if answer == "u":
        user_guess(target)
    elif answer == "c":
        answer = int(input("Pick a number for our CPU to guess: "))
        cpu_guess(answer, max)
    print("Play again?")
    answer = input("y/n: ").lower()
    if answer == "y":
        print("Starting the next round...")
        time.sleep(2)
    elif answer == "n":
        print("See ya later friend!")
        quit()
