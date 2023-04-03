"""Component 4 - game mechanics and looping v3
converting v2 into a function
"""

import random

# function to generate random token
def generate_token(balance):

rounds_played = 0
play_again = ""

# testing loop to generte tokens
while play_again !="x":
    rounds_played += 1
    number = random.randint (1, 100)

    if 1<= number <= 5:
        token = "unicorn"
        balance += 4

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
    return(balance)

# main routine
starting_balance = 5
print("Thanks for playing")
print(f"you started with ${test_amount:.2sf}")
print(f"and you lave with ${balance}")
print("goodbye")
