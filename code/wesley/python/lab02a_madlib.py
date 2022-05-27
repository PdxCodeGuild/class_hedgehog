# Search the internet for an example Mad Lib.
# Ask the user for each word you'll put in your Mad Lib.
# Use string concatenation to combine with user input with other strings to form the Mad Lib.
# Display the Mad Lib to the user.   
noun_1 = input("Enter a noun: ")
plural_noun_1 = input("Enter a plural noun: ")
noun_2 = input("Enter another noun: ")
plural_noun_2 = input("Enter another plural noun: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun_3 = input("Enter another noun: ")

madlib = f"""
Be kind to your {noun_1}-footed {plural_noun_1}
For a duck may be somebody`s {noun_2},
Be kind to your {plural_noun_2} in {place}
Where the weather is always {adjective}.

You may think that this is the {noun_3},
Well it is.
"""

print(madlib)
