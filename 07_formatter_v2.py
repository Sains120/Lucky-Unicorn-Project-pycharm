"""component 5 - statement formatter v2
change v1 into a function
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = (f'{sides} {text} {sides}')
    top_bottom = "*" * len(formatted_text)
    return f"{top_bottom}\n {formatted_text} \n {top_bottom}"

# main routine
text1 = input("Enter the statement you want to format: ")
symbol1 = input("What symbol do you want to use: ")
print()
print(formatter(symbol1, text1))