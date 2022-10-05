"""
Programmer: Ryan Lee
Fizzbuzz interactive
Play fizzbuzz and see how high you can get without making a mistake, or let the computer do it for you!
Rules:
    -Type integers counting upwards from 1 (inclusive)
    -If the number is divisible by 3, instead type Fizz
    -If the number is divisible by 5, instead type Buzz
    -If the number is divisible by both, type FizzBuzz!
    Note: they are not cap sensitive
"""

# A function to type out a full game of fizzbuzz
# Assumes max will be an int on input
def fizzbuzz(max):
    ran = range(max + 1)
    for x in ran:
        result = ""
        if x % 3 == 0:
            result += "Fizz"
        if x % 5 == 0:
            result += "Buzz"
        if result == "":
            print(x)
        else:
            print(result)

# Stores user inputs
answer = ""
# Just syntax
error = True
print("Welcome to FizzBuzz interactive! Would you like to hear the rules?")
while answer != None:
    answer = input("y/n: ").lower()
    if answer == "y":
        print("Rules:\n\
        -Type integers counting upwards from 1 (inclusive) \n\
        -If the number is divisible by 3, instead type Fizz \n\
        -If the number is divisible by 5, instead type Buzz \n\
        -If the number is divisible by both, type FizzBuzz! \n\
        Note: they are not cap sensitive")
        break
    elif answer == "n":
        print("Okay! If you ever change your mind, just type 'rules' to see them later!")
        break
    else:
        print("I'm sorry, I didn't quite catch that. Please answer with y or n")

print("With that out of the way, would you like to play interactive mode (I) or computer mode (C)?")
print("(If you wanna know the difference, type 'help')")
while answer != None:
    answer = input("I/C: ").lower()
    if answer == "i":
        print("Lets play!")
        break
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
        fizzbuzz(answer)
        print("\nAll done!")
        break
    elif answer == 'help':
        print("In interactive mode, you will play fizzbuzz and try to get a highscore as fast as you can without making a mistake!")
        print("In computer mode, you can set the max number and our CPU friend will show you how its done!")
    else:
        print("I'm sorry, I didn't quite catch that. Please answer with I or C")
        print("(If you wanna know the difference, type 'help')")
