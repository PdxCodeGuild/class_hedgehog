# Keenen Pendergraft 
# lab05 - Palindrome and Anagram checker
# May 27 2022

""" Palindrome Checker """

# word_1 = "racecar"

word_1 = input('Enter a word to check if it is a palindrome: ')

if word_1 == word_1 [::-1]:
    print('True')
else:
    print('False')


""" Anagram Checker """

user_1 = input('Enter the first word that you want to check as an anagram: ').lower()

user_2 = input('Enter the second word that you want to check as an anagram: ').lower()

user_1_replace = user_1.replace(" ", "")

user_2_replace = user_2.replace(" ", "")

if sorted(user_1_replace) == sorted(user_2_replace):
    print(f"\n'{user_1}' and '{user_2}' are anagrams.\n")

else:
    print(f"\n'{user_1}' and '{user_2}' are NOT anagrams.\n")