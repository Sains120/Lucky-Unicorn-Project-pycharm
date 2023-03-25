"""yes/no checking function
based on 01_yes_no_v3
"""


# functions go here...
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


# main routine go here...
show_instructions = yes_no("Have you played this game before? ")
print(f"you entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")