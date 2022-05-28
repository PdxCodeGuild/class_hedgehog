


# word = "something"

# #word = "racecar"


# def check_palindrome(word):
#     check_reverse = 0
#     for letter in word:
#         check_reverse = check_reverse - 1
    
#         if letter in word != check_reverse:
#             print(word + "is not a palindrome.")
#             return False
#     return True

# check_palindrome('racecar')



def check_anagram(first_word, sec_word):
    if (type(first_word) != str or type(sec_word) != str):
        raise TypeError("Enter a valid word, with letters!")

    first_word_mix = list(first_word.lower().replace()) 
    sec_word_mix = list(sec_word.lower().replace())

    first_word_mix.sort()
    sec_word_mix.sort()


    if first_word == sec_word:
        print(f"{first_word}, and {sec_word} are anagrams!")
    
    else:
        print(f"{first_word} and {sec_word} are not the same, therefore are not an anagram.")

user_first_word = input("Enter a word: ")
user_sec_word = input("Enter a second word: ")

check_anagram(user_first_word, user_sec_word)