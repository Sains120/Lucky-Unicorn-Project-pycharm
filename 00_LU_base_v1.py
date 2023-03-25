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
    print("Program continues")
    print()


# main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()
else:
    print("Program continues")