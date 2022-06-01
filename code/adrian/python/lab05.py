# PALINDROME
# A palindrome is a word that's the same forwards or backwards, e.g. racecar.
# Another way to think of it is as a word that's equal to its own reverse.

# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.



def check_palindrome():
    "Find out if word is a palindrome"
    user_input = input("Enter a word: ")
    if user_input == user_input[::-1]:
        return f"{user_input} is a palindrome!"
    else:
        return f"{user_input} is not a palindrome"

print(check_palindrome())



# ANAGRAM
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. 
# The procedure for comparing the two strings is as follow:

# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal


def check_anagram(string1, string2):
    "Find out if these strings are anagrams"
    string1 = list(string1.lower().replace(" ", ""))
    string2 = list(string2.lower().replace(" ", ""))
    string1.sort()
    string2.sort()

    if string1 == string2:
        return f"{string1} and {string2} are anagrams!"
    else:
        return "Nope"


print(check_anagram("lis ten", "S ilen t"))