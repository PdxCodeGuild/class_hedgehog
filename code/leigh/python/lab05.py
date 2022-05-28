# lab 05
# Palindrome and anagram
# Leigh Fair-Smiley
# 5/27/2022

def palindrome(word):
    backword = ""
    for x in range(len(word) - 1, -1, -1):
        backword += word[x]
    if backword == word:
        return True
    return False

def anagram(word, word2):
    word = list(word.lower().replace(" ", ""))
    word2 = list(word2.lower().replace(" ", ""))
    word.sort()
    word2.sort()
    if (word == word2):
        return True
    return False


print(palindrome("racecar"))

print(anagram("anagram", "nag a ram"))

