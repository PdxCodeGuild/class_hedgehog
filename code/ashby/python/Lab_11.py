"""
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
"""

"""Version 1"""

import string

def rot_cipher_1():
    
    #Builds library list using string module
    alphabet = list(string.ascii_lowercase)
    #set rot value, stored as variable to modify later
    rot=13
    #inputs text - limited to lowercase
    plain_text = input("Please enter the sentence you would like to encrypt: ")
    plain_list = list(plain_text)
    #iterate through list, check for inclusion in alphabet and modify by +13 index in alphabet list
    for l in range(len(plain_list)):
        if plain_list[l] in alphabet:
            plain_list[l] = alphabet[(alphabet.index(plain_list[l])+rot)%len(alphabet)]
    #rejoins list together for return
    return f"{''.join(plain_list)}"

"""Version 2"""

def rot_cipher_2(): #Allows user to input text to be encrpyted and rotation used in encryption

    #Builds library list using string module
    alphabet = list(string.ascii_lowercase)
    #set rot value, stored as variable to modify later
    
    #inputs text - limited to lowercase
    plain_text = input("Please enter the sentence you would like to encrypt: ")
    while True:
        try:
            rot=int(input("Enter what rotation value would you like for the encryption: "))
        except ValueError:
            print("Invalid rotation cipher. Please enter a number in integer form.")
            continue
        break
    plain_list = list(plain_text)
    #iterate through list, check for inclusion in alphabet and modify by +13 index in alphabet list
    for l in range(len(plain_list)):
        if plain_list[l] in alphabet:
            plain_list[l] = alphabet[(alphabet.index(plain_list[l])+rot)%len(alphabet)]
    #rejoins list together for return
    return f"{''.join(plain_list)}"

"""Version 3"""
# Add support for capital letters, numbers, and special characters.
        
def rot_cipher(): #Allows user to input text to be encrpyted and rotation used in encryption

    #Builds library list using string module
    alphabet = list(string.ascii_lowercase)
    #set rot value, stored as variable to modify later
    
    #inputs text - limited to lowercase
    plain_text = input("Please enter the sentence you would like to encrypt: ")
    while True:
        try:
            rot=int(input("Enter what rotation value would you like for the encryption: "))
        except ValueError:
            print("Invalid rotation cipher. Please enter a number in integer form.")
            continue
        break
    plain_list = list(plain_text)
    #iterate through list, check for inclusion in alphabet and modify by +13 index in alphabet list
    for l in range(len(plain_list)):
        if plain_list[l] in alphabet:
            plain_list[l] = alphabet[(alphabet.index(plain_list[l])+rot)%len(alphabet)]
    #rejoins list together for return
    return f"{''.join(plain_list)}"

print(rot_cipher())