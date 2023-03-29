"""Component 3 (random tokens) v4
Calculate percentages to ensure the adds favour house
5% unicorns, 30% donkeys, and the remaining 65% horse/zebra
"""

import random


starting_balance = 100
balance = starting_balance

# testing loop to generate 100 tokens
for item in range(10):
    number = random.randint(1,100)

    # adjust balance
    # if the random number is between 1 and 5
    # user gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    elif 6<= number <= 36:
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
    print(f"Token: {token}, Balance: ${balance:.2f}")
print(f"Starting balance = ${starting_balance:.2f}")
print(f"Final balance = ${balance:.2f}")