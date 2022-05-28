
"""Palindrome Check"""

"""Write a function check_palindrome which takes a string, 
and returns True if the string's a palindrome, or False if it's not."""
#Fun fact: The fear of palindromes is called Aibohphobia, which is a palindrome itself. That is pretty messed up.

def palindrome_check(input):
    from string import punctuation as punc
    strip_list = list(punc)
    #adds " " to striplist
    strip_list.append(" ")
    #strip input of random biz
    for x in strip_list:
        input = input.replace(x, "")
    #save as two separate check variables, reverse second one
    test_1 = input.lower()
    test_2 = input.lower()[::-1]
    #Return boolean value
    return test_1 == test_2


"""Anagram Checker"""

"""Write another function check_anagram that takes two strings as parameters 
and returns True if they're anagrams of eachother, False if they're not. 
The procedure for comparing the two strings is as follow:"""

def anagram_check(input_1, input_2):
    #pulls punctuation list to strip inputs
    from string import punctuation as punc
    strip_list = list(punc)
    #adds " " to striplist
    strip_list.append(" ")
    #strips all excess characters from striplist  
    for x in strip_list:
        input_1 = input_1.replace(x, "")
    for x in strip_list:
        input_2 = input_2.replace(x, "")
    # prepare data for checks
    checklist_1 = list((input_1).lower())
    checklist_2 = list((input_2).lower())
    #list sorter
    checklist_1.sort()
    checklist_2.sort()
    #return True or false statement
    return (checklist_1 == checklist_2)  

# Fun interface for fun

print(f"""
Hello! Please select from the following options:

1. Palindrome checker
2. Anagram checker
3. Exit
 """)

while True:
    user_input = input("Please enter your number selection here: ")
    if user_input == "1":
        
        word_1 = input("Welcome to the palindrome checker!\nPlease type in the word you would like to check: ")
        if palindrome_check(word_1):
            print(f"{word_1} is a palindrome! Congratulations!")
            break
        else: 
            print(f"{word_1} is not a palindrome.")
            break
    elif user_input =="2":
        word_1 = input("\nPlease type in your first word: ")
        word_2 = input("\nPlease type in your second word: ")

        if anagram_check(word_1,word_2) == True:
            print(f"{word_1} and {word_2} are anagrams! Yay!")
            break
        else: 
            print(f'Unfortunately, {word_1}and {word_2} are not anagrams.')
            break
    elif user_input =="3":
        print("Have a good day!")
        break
    else:
        print("I am afraid that is not an option, please try again!")