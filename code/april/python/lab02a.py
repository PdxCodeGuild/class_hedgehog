"""
Lab 02a
April
25 May 2022
"""

# Search the internet for an example Mad Lib.
"""
Dear School Nurse:
{silly_word_1} {last_name} will not be attending school today. 
He/she has come down with a case of {illness} and has horrible {plural_noun} 
and a/an {adjective_1} fever. We have made an appointment with the 
{adjective_2} Dr. {silly_word_2}, who studied for many years in {place} 
and has {number} degrees in pediatrics. He will send you all the 
information you need. Thank you!

Sincerely
Mrs. {adjective_3}. 
"""

# Ask the user for each word you'll put in your Mad Lib.

silly_word_1 = input("Enter a silly word: ")
last_name = input("Enter a last name: ")
illness = input("Enter an illness: ")
plural_noun = input("Enter a plural noun: ")
adjective_1 = input("Enter an adjective: ")
adjective_2 = input("Enter another adjective: ")
silly_word_2 = input("Enter another silly word: ")
place = input("Enter a place: ")
number = input("Enter a number: ")
adjective_3 = input("Enter another adjective: ")

# Use string concatenation to combine with 
# user input with other strings to form the Mad Lib.
madlib = f"""
Dear School Nurse:
{silly_word_1} {last_name} will not be attending school today. 
He/she has come down with a case of {illness} and has horrible {plural_noun} 
and a/an {adjective_1} fever. We have made an appointment with the 
{adjective_2} Dr. {silly_word_2}, who studied for many years in {place} 
and has {number} degrees in pediatrics. He will send you all the 
information you need. Thank you!

Sincerely
Mrs. {adjective_3}. 
"""

# Display the Mad Lib to the user.

print(madlib)




