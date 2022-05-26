# Mad Libs
# Write a simple program that prompts the user for several inputs then prints a 
# Mad Lib as the result. You can find inspiration here.

# Instructions
# Search the internet for an example Mad Lib.
# Ask the user for each word you'll put in your Mad Lib.
# Use string concatenation to combine with user input with other strings to form the Mad Lib.
# Display the Mad Lib to the user.
# Example Run
# Give me an antonym for 'data': nonmaterial Tell me an adjective: Bearded Give me a 
# sciency buzzword: half-stack A type of animal (plural): parrots Some Sciency thing: 
# warp drive Another sciency thing: Trilithium crystals Sciency adjective: biochemical

# Nonmaterial Scientist Job Description: Seeking a bearded engineer, able to work on 
# half-stack projects with a team of parrots. Key responsibilities:

# Extract patterns from non-material
# Optimize warp drive
# Transform trilithium crystals into biochemical material.

# noun bath , plural noun courts, noun board, place Monterey, adjective front, noun beau
# Be kind to your Bath-footed Courts
# For a duck may be somebody`s Board,
# Be kind to your Courts in Monterrey
# Where the weather is always Front.
# You may think that this is the Beau,
# Well it is.


mad1 = input("Enter a noun: \n\t> ")
mad2 = input("Enter a plural noun: \n\t> ")
mad3 = input("Enter a noun: \n\t> ")
mad4 = input("Enter a place: \n\t> ")
mad5 = input("Enter am adjective: \n\t> ")
mad6 = input("Enter a noun: \n\t> ")

madlib = f"""Be kind to your {mad1}-footed {mad2}
For a duck may be somebody's {mad3},
Be kind to your {mad2} in {mad4}
Where the weather is always {mad5}.

You may think that this is {mad6},
well it is."""
print(madlib)


# Version 2 (optional)
# Make a functional solution that utilizes lists. For example, ask the user for 3 
# adjectives, separated by commas, then use the .split() function to store each 
# adjective and later use it in your story.

# Add randomness! Use the random module, rather than selecting which adjective goes where in the story.





# Version 3 (optional)
# Make it repeatable. Once you're done prompting the user for words, prompt them 
# for whether they'd like to hear the story. Use a while loop to keep asking if they'd 
# like to hear the story again until the answer is 'no'. You could then ask them if they'd 
# like to make another story, and so on.

