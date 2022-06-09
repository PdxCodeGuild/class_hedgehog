#Rot Cipher version 1, 2, and kind of 3

import string   #replaces manual dictionary
def main():     #function for taking in user input
    user_input = input("Enter word or phrase to be encrypted: ")
    while True:
        try:
            encrypt = int(input("Enter the number of cypher shifts: "))
            break
        except:
            print("Something went wrong, try again.")
            
    enc_str = encrypt_string(encrypt, user_input) #Calls on other function to encrypt user inputs
    print(''.join(enc_str)) #joins encryption output list into a single string
def encrypt_string(num, str): #function that takes the user input and does the encryption
    encrypted = []
    for char in str:
        while (ord(char)) + num > 122:
            num = num - 26
        encrypted.append(chr(ord(char) + num))
    return encrypted
main()