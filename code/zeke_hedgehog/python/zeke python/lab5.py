"""Lab 5: Palindrome and Anagram
Let's write a palindrome and anagram checker.

Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome

"""


# palindrome = input("enter a word: ")

def check_palindrome(string):
    word = list(string)
    reversed_word = word[::-1]

    return word == reversed_word
    

print(check_palindrome("level"))
print(check_palindrome("potato"))

"""

Anagram
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams


"""

def check_anagram(string1, string2):
# Convert each word to lower case (lower)
    string1 = string1.lower()
    string2 = string2.lower()
# Remove all the spaces from each word (replace)
    string1 = string1.replace(" "," " )
    string2 = string2.replace(" "," ")
# Sort the letters of each word (sorted)
    list1 = sorted(string1)
    string2 = string2.lower()
# Check if the two are equal
