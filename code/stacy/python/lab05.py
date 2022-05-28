def check_palindrome(word):
    reverse_index = 0
    for letter in word:
        reverse_index -= 1
        if letter != word[reverse_index]:
            return False
    return True
#word = input("Enter a word: \n\t> ")
#print(check_palindrome(word))
def check_anagram(word_1, word_2):
    word_1 = word_1.replace(' ','').lower()
    word_2 = word_2.replace(' ','').lower()
    list_1 = list(word_1)
    list_2 = list(word_2)
    list_1.sort()
    list_2.sort()
    if list_1 == list_2:
        return True
    else:
        return False
# word_1 = input("Enter first word: \n\t> ")
# word_2 = input("Enter second word: \n\t> ")
# print(check_anagram(word_1, word_2))
###############################################################################################################
'''
# Lab 5: Palindrome and Anagram
# Let's write a palindrome and anagram checker.
# Palindrome
# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.
# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.
# >>> enter a word: racecar
# >>> 'racecar' is a palindrome
# >>> enter a word: palindrome
# >>> 'palindrome' is not a palindrome
###############################################################################################################
# Anagram
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.
# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:
# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal
# >>> enter the first word: anagram
# >>> enter the second word: nag a ram
# >>> 'anagram' and 'nag a ram' are anagrams
'''