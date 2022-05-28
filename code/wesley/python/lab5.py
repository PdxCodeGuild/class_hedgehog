# A palindrome is a word that's the same forwards or backwards, e.g. racecar. 
# Another way to think of it is as a word that's equal to its own reverse.

# Write a function check_palindrome which takes a string, and 
# returns True if the string's a palindrome, or False if it's not.


def check_palindrome(word):
    word_list = (list(word))
    word_rev = (list(reversed(word_list)))

    if word_list == word_rev:
        return (f"{word} is a palindrome!")
    elif word_list != word_rev:
        return (f"{word} is not a palindrome!")


user_word = input("Enter a word: ")

print(check_palindrome(user_word))


def check_anagram(first_word, second_word):
    first_low = first_word.lower()
    second_low = second_word.lower()
    first_rep = first_low.replace(" ", '')
    second_rep = second_low.replace(" ", '')
    first_list = list(sorted(first_rep))
    second_list = list(sorted(second_rep))
    
    if first_list == second_list:
        return (f"{first_word} and {second_word} are anagrams.")
    else:
        return (f"{first_word} and {second_word} are not anagrams.")


first_word = input(f">>> enter the first word: ")
second_word = input(">>> enter the second word: ")

print(check_anagram(first_word,second_word))