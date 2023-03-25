# ask the user if they have played before
show_instructions = input("Have you played before? : ")

# if they say yes, output 'program continues'
if show_instructions == "yes":
    print("Program continues")

# if they say no, output 'display instructions'
elif show_instructions == "no":
    print("Display instructions")

# otherwise - show error
else:
    print("Please enter 'Yes' or 'No'")
