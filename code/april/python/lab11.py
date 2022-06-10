"""
Lab 11
Rot Cipher

Write a program that prompts the user for a string, 
and encodes it with ROT13. For each character, find 
the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, 
so encryption is the same as decryption.
"""
import string

# def rot_cipher():
#     alphabet = list(string.ascii_lowercase)
#     # create encoded to hold our encrypted word
#     encoded = ''
#     # prompts for user to input string
#     user_input = input("Please enter a string: ").lower()
#     rot13 = 13

#     # for each character, find corresponding character and 
#     # add it to an output string
#     for item in user_input:
#         if item in alphabet:
#             letter = (alphabet.index(item) + rot13) % 26
#             encoded += alphabet[letter]
#         else: # to allow for characters other than letters
#             encoded += item

#     print(f"User string: {user_input}\nEncoded string: {encoded} ")

# rot_cipher()        
 

"""
Version 2

Allow the user to input the amount of rotation used in 
the encryption. (ROTN)
"""

def rot_cipher():
    alphabet = list(string.ascii_lowercase)
    encoded = ''
    user_input = input("Please enter a string: ").lower()
    # allow user to choose rotation
    rot_choice = int(input("Please enter how many rotations: ")) 

    for item in user_input:
        if item in alphabet:
            letter = (alphabet.index(item) + rot_choice) % 26
            encoded += alphabet[letter]
        else: # to allow for characters other than letters
            encoded += item

    print(f"User string: {user_input}\nEncoded string: {encoded} ")

rot_cipher()    


"""
Version 3 (optional)

Add support for capital letters, numbers, and special characters. 
These can be handled in two different ways:

1. Capital letters can be rotated as well, numbers and special 
characters can be put directly into the output (e.g. "hello world!" 
becomes "uryyb jbeyq!").

2. Instead of using an alphabet of just letters, include numbers, 
spaces, and special characters as well.
"""

# string.ascii_uppercase