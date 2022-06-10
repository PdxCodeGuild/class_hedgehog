#
# 
#  # Rot Cipher

# Write a program that prompts the user for a string, and encodes it with ROT13. 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.


# | Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
# |---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
# | English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v| w| x| y| z|
# | ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i| j| k| l| m|

import string

def ROT():
    import string
    alphabet = list(string.ascii_lowercase)

    user_cipher = input("Enter a the phrase or passage you would like to encrypt: ").lower().replace(string.punctuation, "_")
    ROT_inc = int(input("Enter the value you would like to increment your cipher by (ROT number): "))
   
    encrypted_string = ""
    
    for ch in user_cipher:
        if ch in alphabet:
            cipher_value = (alphabet.index(ch) + ROT_inc) % 26
            encrypted_string += ''.join(alphabet[cipher_value]) 

        else:
            encrypted_string += ch
    
    return encrypted_string


ROT()
    
#     import string  
#     ROT_inc = input("Enter the value you would like to increment your cipher by (ROT number): ")
#     user_cipher = (ROT(input("Enter a the phrase or passage you would like to encrypt: ").lower().replace(string.punctuation, ""), int(ROT_inc)))
#     print(user_cipher)
#     print("Do you have another item to encrypt, Y or N?")
#     again = input(">: ").upper()
#     if again == "Y":
#         main()
#     else:
#         quit(0)
# main()

  # alphabet = {
    #     0: "a",
    #     1: "b",
    #     2: "c",
    #     3: "d",
    #     4: "e",
    #     5: "f",
    #     6: "g",
    #     7: "h",
    #     8: "i",
    #     9: "j",
    #     10: "k",
    #     11: "l",
    #     12: "m",
    #     13: "n",
    #     14: "o",
    #     15: "p",
    #     16: "q",
    #     17: "r",
    #     18: "s",
    #     19: "t",
    #     20: "u",
    #     21: "v",
    #     22: "w",
    #     23: "x",
    #     24: "y",
    #     25: "z",
    # }

    # inc_alpha = {
    #     "a": 0,
    #     "b": 1,
    #     "c": 2,
    #     "d": 3,
    #     "e": 4,
    #     "f": 5,
    #     "g": 6,
    #     "h": 7,
    #     "i": 8,
    #     "j": 9,
    #     "k": 10,
    #     "l": 11,
    #     "m": 12,
    #     "n": 13,
    #     "o": 14,
    #     "p": 15,
    #     "q": 16,
    #     "r": 17,
    #     "s": 18,
    #     "t": 19,
    #     "u": 20,
    #     "v": 21,
    #     "w": 22,
    #     "x": 23,
    #     "y": 24,
    #     "z": 25
    # }

  







# ## Version 2

# Allow the user to input the amount of rotation used in the encryption. (ROTN)

# ## Version 3 (optional)

# Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

# 1. Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

# 2. Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.