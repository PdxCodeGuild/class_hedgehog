#Palindrome
"""
word = input("Please enter a word: ")

def check_palindrome(word):

    if(word == word[:: - 1]):
        print("The word entered is a Palindrome")
    else:
        print("This word entered is not a Palindrome")

check_palindrome(word)

#Anagram
"""
word1 = input("Enter a word: ").lower()
word2 = input("Enter the second word: ").lower()
word1 = word1.replace(" ", "" )
word2 = word2.replace(" ", "" )


def check_anagram(word1, word2):
       
    if(sorted(word1)== sorted(word2)):
        print("These are anagrams.")
    else:
        print("The aren't anagrams.")        
         
check_anagram(word1, word2)


