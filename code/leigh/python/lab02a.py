# Lab 02a
# Mad libs
    # Search the internet for an example Mad Lib.
    # Ask the user for each word you'll put in your Mad Lib.
    # Use string concatenation to combine with user input with other strings to form the Mad Lib.
    # Display the Mad Lib to the user.
# Leigh Fair-Smiley
# 5/25/2022

noun_one = input("Give me a noun!: ")
noun_two = input("Give me a plural noun!: ")
noun_three = input("Give me another noun!: ")
place = input("Give me a place!: ")
adjective = input("Give me an adjective!: ")
noun_four = input("Give me another noun!: ")

print(f"""Be kind to your {noun_one}-footed {noun_two}
For a duck may be somebody's {noun_three},
Be kind to your {noun_two} in {place}
Where the weather is always{adjective}.
You may think that this is the {noun_four},
Well it is.""")