"""Lu yes/no
simplifies the input by converting it to lowercase.
Also, accepts y or n as abbreviations.
Prints result of user choice as well as input - for testing"""

show_instructions = ""
while show_instructions != "x":

    # ask the user if they have played before
    show_instructions = input("Have you played before? : ").lower()

    # if they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # if they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":\
        print("Display instructions")

    # otherwise - show error
    else:
        print("Please enter 'Yes' or 'No'")

    print(f"You entered '{show_instructions}'")