"""
A palindrome is a word that's the same forwards or
backwards, e.g. racecar. Another way to think of it
is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string,
and returns True if the string's a palindrome,
or False if it's not.
"""


# def check_palindrome(string):
#     word = list(string)
#     reversed_word = word[::-1]

#     if word == reversed_word:
#         return True
#     else:
#         return False


def check_palindrome(string):
    reversed_word = string[::-1]
    return string == reversed_word


is_palindrome = check_palindrome("level")
# print(is_palindrome)
# print(check_palindrome("potato"))


"""
Two words are anagrams of eachother if the letters of one can be
rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as
parameters and returns True if they're anagrams of eachother, False
if they're not. The procedure for comparing the two strings is as follow:
"""


# def check_anagram(string1, string2):
#     # Convert each word to lower case (lower)
#     string1 = string1.lower()
#     string2 = string2.lower()

#     # Remove all the spaces from each word (replace)
#     string1 = string1.replace(" ", "")
#     string2 = string2.replace(" ", "")

#     # Sort the letters of each word (sorted)
#     # list1 = list(string1)
#     # list1.sort()
#     list1 = sorted(string1)
#     list2 = sorted(string2)

#     # Check if the two are equal
#     return list1 == list2

def check_anagram(string1, string2):
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    return sorted(string1) == sorted(string2)


print(check_anagram("anagram", "nag a ram"))
print(check_anagram("hedgehog", "sonic"))
