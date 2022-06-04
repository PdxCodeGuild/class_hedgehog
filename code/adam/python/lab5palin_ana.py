


# word = "something"

# #word = "racecar"

def check_palindrome(word):
    # word = list(string)
    # rev_word = word.reverse()
    rev_word = word[::-1]
    return rev_word == word
   
pal_word = input("Enter the word you would like to check: ")
print(check_palindrome(pal_word))



def check_anagram(first_word, sec_word):
    if (type(first_word) != str or type(sec_word) != str):
        raise TypeError("Enter a valid word, with letters!")

    first_word_mix = list(first_word.lower().replace(" ", "")) 
    sec_word_mix = list(sec_word.lower().replace(" ", ""))

    first_word_mix.sort()
    sec_word_mix.sort()


    return first_word == sec_word
        

user_first_word = input("Enter a word: ")
user_sec_word = input("Enter a second word: ")

print(check_anagram(user_first_word, user_sec_word))