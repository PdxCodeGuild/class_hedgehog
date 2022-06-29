"""
Write a program that prompts the user for a string, and encodes
it with ROT13. For each character, find the corresponding character,
add it to an output string. Notice that there are 26 letters in the
English language, so encryption is the same as decryption.
"""

import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = string.punctuation


def rotate(letter, char_set=lowercase, rotation=13):
    if letter in char_set:
        index = char_set.index(letter) + rotation
        return char_set[index % len(char_set)]
    else:
        return letter


# Get original string from user
# Format input to be lowercase
message = input("Enter input string: ")
rotation = int(input("Enter amount of rotation: "))
# Rotate letters by 13, leave other characters as they were
output = ""
# iterate over input
for letter in message:
    # check each letter to see if it is in string.ascii_lowercase
    if letter in lowercase:
        output += rotate(letter, rotation=rotation)
    elif letter in uppercase:
        output += rotate(letter, uppercase, rotation)
    elif letter in digits:
        output += rotate(letter, digits, rotation)
    elif letter in special:
        output += rotate(letter, special, rotation)
    else:
        output += letter
# print output
print(output)
