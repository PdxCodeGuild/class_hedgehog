"""
Lab 5 
April
27 May 2022
"""

""" Palindrome """

# user_input = input("Enter a word: ") # prompt user to input word to check

# def check_palindrome(user_input): # defining function
#     backwards = 0 # create variable for backwards word
#     for forwards in user_input: 
#         backwards = backwards -1 # take the word and reverse it
#         #palindrome
#         if forwards == user_input[backwards]: # if forwards is equal to backwards it is 'True'
#             print(f"{user_input.title()} is a palindrome." ) # print statement 
#             return True  
#         #not palindrome
#         elif forwards != user_input[backwards]: # if forwards is not equal to backwards it is 'False'
#             print(f"{user_input.title()} is not a palindrome." ) # print statement
#             return False
   
            
# check_palindrome(user_input) # call function


""" Anagagram """

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")


def check_anagram(word1, word2):

    word1b = word1
    word2b = word2

    # convert to lower case and remove spaces
    word1b = word1b.lower().replace(" ", "")
    word2b = word2b.lower().replace(" ", "")
 
    # sort the letters of each word
    word1b = sorted(word1b)
    word2b = sorted(word2b)

    # check if the two are equal
    if word1b == word2b: # if they are equal they are 'True' -- they are anagrams
        print(f"'{word1.title()}' and '{word2}' are anagrams.")
        return True
    elif word1b != word2b: # if they are not equal they are 'False' -- they are not anagrams
        print(f"'{word1.title()}' and '{word2}' are not anagrams.")   
        return False


check_anagram(word1, word2) # call function
