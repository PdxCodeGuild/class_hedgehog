"""
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result. You can find inspiration here.

Instructions
Search the internet for an example Mad Lib.
Ask the user for each word you'll put in your Mad Lib.
Use string concatenation to combine with user input with other strings to form the Mad Lib.
Display the Mad Lib to the user.    
"""

#Recieve input from user for madlib
adjective_1 = input("Enter an adjective: ")
italian_name = input("Enter an Italian name: ")
occupation = input("Enter an occupation: ")
verb_ending_ing = input("Enter a verb ending in 'ing': ")
plant_plural = input("Enter a plant (plural): ")
adjective_2 = input("Enter another adjective: ")
plural_noun = input("Enter a plural noun: ")
noun = ("Enter a singular noun please: ")
person_in_room = input("Enter the name of a person in the room: ")




madlib = f"""{adjective_1} {italian_name} Brothers is a popular video game where you control a/an {occupation} as 
he/she runs through levels {verb_ending_ing} on enemies and eating {plant_plural} to get {adjective_2} and 
fireflowers so that he/she can throw {plural_noun} at enemies. 
He does all this to save the {noun} from the evil {person_in_room}."""

print(madlib)