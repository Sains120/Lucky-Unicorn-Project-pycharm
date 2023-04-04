"""LU Base component - based on 00_LU_base_v2
Components added after they have been created and tested
"""
import random

# yes/no checking function
def yes_no(questions_text):
    while True:

        # ask the user if they have played before
        answer = input(questions_text).lower()

        # if they say yes, output 'program continues'
        if answer == "yes" or answer == "y":
            answer = "yes"
            return answer

        # if they say no, output 'display instructions'
        elif answer == "no" or answer == "n":
            answer = "no"
            return answer

        # otherwise - show error
        else:
            print("Please enter 'Yes' or 'No'")


#function to display instructions
def instructions():
    print("***** How to play *****")
    print()
    print("The rules of the game will go here")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = (int(input(question)))

            # check for number within required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# function to generate random token
def generate_token(balance):...

    rounds_played = 0
    play_again = ""

    # testing loop to generate tokens
    while play_again != "x":
        rounds_played += 1
        number = random.randint(1, 100)

        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        else:
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.5
            else:
                token = "horse"
                balance -= 0.5

        # output
        print(f"round: {rounds_played}. Token: {token}. Balance: ${balance:.2sf}")
        if balance < 1:
            print("\n Sorry you have run out of money.")
            play_again = "x"
        else:
            play_again = input("\n Do you want to play another round? \n <enter> to play again or 'x' to exit.").lower()
        print()
    return balance


# function to format text output
def formatter(symbol, text):...


# main routine go here...
print(formatter("-", "Welcome to the lucky unicorn game"))
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()


# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with $ ", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"you started with ${starting_balance:.2sf}")
print(f"and you lave with ${closing_balance:.2sf}")
print()
print(formatter("*", "Goodbye"))