"""
Programmer: Ryan Lee
Fizzbuzz interactive
Play fizzbuzz and see how high you can get without making a mistake, or let a CPU show you how its done!
Rules:
    -Type integers counting upwards from 1 (inclusive)
    -If the number is divisible by 3, instead type Fizz
    -If the number is divisible by 5, instead type Buzz
    -If the number is divisible by both, type FizzBuzz!
    Note: they are not cap sensitive
"""

# A function to type out a full game of fizzbuzz
# Assumes max will be an int on input
def fizzbuzz(max, mode):
    ran = range(max + 1)
    for x in ran:
        result = ""
        if x % 3 == 0:
            result += "Fizz"
        if x % 5 == 0:
            result += "Buzz"
        if mode == "computer":
            if result == "":
                print(x)
            else:
                print(result)

# Just a function to print out the play again text after a completed game
def play_again():
    answer = ""
    while answer != None:
        print("Play again?")
        answer = input("y/n: ").lower()
        if answer == "y":
            print("Okay! Interactive or Computer mode?")
            return
        elif answer == "n":
            print("I hope you had fun! Bye for now friend")
            quit()
        else:
            print("Sorry, I didn't quite catch that")

# rules for the game
rules = "\nRules:\n\
        -Type integers counting upwards from 1 (inclusive) \n\
        -If the number is divisible by 3, instead type Fizz \n\
        -If the number is divisible by 5, instead type Buzz \n\
        -If the number is divisible by both, type FizzBuzz! \n\
        Note: they are not cap sensitive\n"
# Stores user inputs
answer = ""
# Just syntax
error = True
print("Welcome to FizzBuzz interactive! Would you like to hear the rules?")
answer = input("y/n: ").lower()
if answer == "y":
    print(rules)
    print("To see them again, just type 'rules'\n")
elif answer == "n":
    print("Okay! If you ever change your mind, just type 'rules' to see them later!\n")
else:
    print("I'm sorry, I didn't quite catch that. Please answer with y or n")

print("With that out of the way, would you like to play interactive mode (I) or computer mode (C)?")
print("(If you wanna know the difference, type 'help')")
print("To exit, type 'quit'")
while answer != None:
    answer = input("I/C: ").lower()
    if answer == "rules":
        print(rules)
    elif answer == "quit":
        print("See you later friend!")
        quit()
    elif answer == "i":
        print("Lets play!")
        print("To stop the game early, type 'quit' at any time")
        print("Starting from 1, lets see how high you can go!")
        # Current stores the current value the player is on
        current = 1
        while answer != "quit":
            # Result will hold the correct answer
            result = ""
            answer = input("Answer: ").lower()
            if current % 3 == 0:
                result += "fizz"
            if current % 5 == 0:
                result += "buzz"
            if result == "":
                result = str(current)
            if answer == result:
                print("Correct!")
                current += 1
            elif answer == "quit":
                print(f"Your score is: {current - 1}\n")
            elif answer == "rules":
                print(rules)
            else:
                print(f"Sorry, that wasnt the right answer! The correct answer was: {result}")
                print(f"Your score is: {current - 1}\n")
                break
        play_again()
    elif answer == "c":
        print("Sounds good!")
        print("How high should the computer go?")
        while error:
            try:
                answer = int(input("Please type a number: "))
            except ValueError:
                print("Error: Please only use numbers")
                continue
            break
        fizzbuzz(answer, "computer")
        print("\nAll done!")
        play_again()
    elif answer == 'help':
        print("In interactive mode, you will play fizzbuzz and try to get a highscore as fast as you can without making a mistake!")
        print("In computer mode, you can set the max number and our CPU friend will show you how its done!")
    else:
        print("I'm sorry, I didn't quite catch that. Please answer with I or C")
        print("(If you wanna know the difference, type 'help')")
