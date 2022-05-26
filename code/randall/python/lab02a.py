"""
1. Search the internet for an example Mad Lib.

Be kind to your {NOUN}-footed {PURAL NOUN}
For a {NOUN} may be somebody`s Message,
Be kind to your {PURAL NOUN} in {place}
Where the {adjective} is always {noun}.

You may think that this is the Innocence,
Well it is.

2. Ask the user for each word you'll put in your Mad Lib.
3. Use string concatenation to combine with user input with other strings to form the Mad Lib.
4. Display the Mad Lib to the user.
"""

one = input("Enter a noun: ")
two = input("Enter a plural noun: ")
three = input("Enter another noun: ")
four = input("Enter another plural noun: ")
five = input("Enter a place: ")
six = input("Enter an adjective: ")
seven = input("Enter another noun: ")

madlib = f"""Be kind to your {one}-footed {two}
For a {three} may be somebody`s Message, Be kind
to your {four} in {five} Where the {six} is always {seven}.

You may think that this is the {seven},
Well it is.
"""
print(madlib)