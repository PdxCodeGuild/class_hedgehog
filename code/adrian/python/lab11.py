import random 
import string
# Write a program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, 
# so encryption is the same as decryption.




# abc = string.ascii_letters

# dictionary of alphabet and Rot+13
# letters = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",  "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m",}

# def rot():
#     # user input
#     word = input("Pick a word: ")

#     # convert word to string of letters
#     for letter in word:
#         # print out corresponding character
#         print(letters.get(letter))

# rot()




# Version 2 (I had trouble figuring it out with dictionary so just imported string ascii)



message = input("Enter a message: ")
user_rot = int(input("Enter rotation amount: "))

def rot(text, amount):
    abc = string.ascii_lowercase
    encrypt = ""
    for ch in text:
        if ch == " ":
            encrypt = encrypt + " "
        else:
            rotate = abc.index(ch) + int(amount)
            if rotate < 26:
                encrypt = encrypt + abc[rotate]
            else:
                encrypt = encrypt + abc[rotate % 26]
    return encrypt


print(rot(message, user_rot))