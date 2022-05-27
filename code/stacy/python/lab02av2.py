# Version 2 (optional)
# Make a functional solution that utilizes lists. For example, ask the user for 3 
# adjectives, separated by commas, then use the .split() function to store each 
# adjective and later use it in your story.

# Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
import random
list_of_adjectives = input("Please enter adjectives separated by commas: \n\t> ").split(',')
list_of_nouns = input("Please enter nouns separated by commas: \n\t> ").split(',')
madlib = f"""Be kind to your {random.choice(list_of_nouns)}-footed {random.choice(list_of_nouns)}
For a duck may be somebody's {random.choice(list_of_nouns)},
Be kind to your {random.choice(list_of_nouns)} in {random.choice(list_of_nouns)}
Where the weather is always {random.choice(list_of_adjectives)}.

You may think that this is {random.choice(list_of_nouns)},
well it is."""
print(madlib)
