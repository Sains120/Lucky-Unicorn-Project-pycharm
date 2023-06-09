"""Component 3 (random tokens) v3
Format currency
Ensure adds favour the house - 10% chance of unicorn and 30% chance for each of
donkey, zebra, or horse
"""

import random

tokens = ["unicorn",
          "horse", "horse", "horse",
          "donkey", "donkey", "donkey",
          "zebra", "zebra", "zebra"]

starting_balance = 100
balance = starting_balance

# testing loop to generate 100 tokens
for item in range(500):
    token = random.choice(tokens)

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    # output
print(f"Starting balance = ${starting_balance:.2f}")
print(f"Final balance = ${balance:.2f}")