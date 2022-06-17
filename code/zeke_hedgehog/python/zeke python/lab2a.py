

# Search the internet for an example Mad Lib.

"""
Be kind to your {noun}-footed {plural Noun}
For a duck may be somebody`s {noun},
Be kind to your {plural noun} in {place}
Where the weather is always {adjective}.

You may think that this is the {noun},
Well it is.

"""
# Ask the user for each word you'll put in your Mad Lib.
noun_1 = input('Enter a noun: ')
plural_noun_1 = input('Enter a plural noun: ')
noun_2 = input('Enter another noun: ')
plural_noun_2 = input('Enter another plural noun: ')
place_1 = input('Enter a place: ')
adjective = input('Enter an adjective: ')
noun_3 =input('Enter another noun: ')

# Use string concatenation to combine with user input with other strings to form the Mad Lib.

madlib = f""" Be kind to your {noun_1}-footed {plural_noun_1}  
For a duck may be somebody`s {noun_2},
Be kind to your {plural_noun_2} in {place_1}
Where the weather is always {adjective}.
You may think that this is the {noun_1},
Well it is.

"""
# Display the Mad Lib to the user.

print(madlib)


