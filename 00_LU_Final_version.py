"""LU Base component - based on 00_LU_base_v3
Adding instructions to instructions function and further text decorations
including round number and token
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
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter> to play. You will get a random token which may be a"
          " horse, a donkey, a zebra, or a unicorn.")
    print()
    print("It costs $1 to play each round but, depending on your price, you may get some of your money "
          "back.\nThese are the payout amounts: \n"
          "\tUnicorn: $5 (balance increased by $4)\n"
          "\tZebra $0.50 (balance decreased by $0.50)\n"
          "\tHorse $0.50 (balance decreased by $0.50)\n"
          "\tDonkey $0 (balance decreased by $1)\n")
    print("\n See if you can avoid donkeys, get the unicorns, and finish with more money "
          "than you started with.\n")
    print("*" * 50)
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
    print(formatter(".", f"Round: {rounds_played}"))
    print()
    number = random.randint(1, 100)

    if 1 <= number <= 5:
        balance += 4
        print(formatter("!", "Congratulations, you got a unicorn"))
        print()

    elif 6 <= number <= 36:
        balance -= 1
        print("Bad luck you got a donkey.")
        print()

    else:
        if number % 2 == 0:
            balance -= 0.5
            print("You got a zebra")
            print()
        else:
            balance -= 0.5
            print("You got a horse")
            print()

        # output
        print(f"Your balance is now: ${balance:.2sf})
        if balance < 1:
            print("\n Sorry you have run out of money.")
            play_again = "x"
        else:
            play_again = input("\n Do you want to play another round? \n <enter> to play again or 'x' to exit.").lower()
        print()
    return balance


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formated_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formated_text)
    return f"{top_bottom}\n {formated_text}\n {top_bottom}"


# main routine go here...
print(formatter("-", "Welcome to the lucky unicorn game"))
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()


# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with $ ", 1, 10)
print(f"You are playing with ${starting_balance:.2sf}\n")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"you started with ${starting_balance:.2sf}")
print(f"and you lave with ${closing_balance:.2sf}")
print()
print(formatter("*", "Goodbye"))