"""LU Base component
Components added after they have been created and tested"""


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


# main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()


# ask the user how much they want to play with
user_balance = num_check("How much would you like to play with $ ", 1, 10)
print(f"You are playing with ${user_balance}")