# Version 3 (optional)
# Make it repeatable. Once you're done prompting the user for words, 
# prompt them for whether they'd like to hear the story. Use a while 
# loop to keep asking if they'd like to hear the story again until the 
# answer is 'no'. You could then ask them if they'd like to make another story, and so on.
import random
while True:
    list_of_nouns = input("Please enter nouns separated by commas: \n\t> ").split(',')
    list_of_adjectives = input("Please enter adjectives separated by commas: \n\t> ").split(',')
    hear_story = input("Type y and press enter to hear the story. Type anything else and press enter to exit.").lower().replace(' ','')
    if hear_story == 'y':
        madlib = f"""Be kind to your {random.choice(list_of_nouns)}-footed {random.choice(list_of_nouns)}
        For a duck may be somebody's {random.choice(list_of_nouns)},
        Be kind to your {random.choice(list_of_nouns)} in {random.choice(list_of_nouns)}
        Where the weather is always {random.choice(list_of_adjectives)}.

        You may think that this is {random.choice(list_of_nouns)},
        well it is."""
        print(madlib)
    else:
        break
    another_madlib = input("If you would like to make another madlib, type y and press enter. Otherwise, type anything else and press enter: \n\t> ").lower().replace(' ','')
    if another_madlib != 'y':
        break