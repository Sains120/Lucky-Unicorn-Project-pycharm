"""Component 4 - game mechanics and looping v2
based on 06_rounds_v1
removed hard-wiring so that all tokens can be allocated (randint 1-100)
gives user feedback about number of rounds and maintains balance
test amount set to $5
"""

import random

# main routine
test_amount = 5
balance = test_amount

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
