

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    text = text.upper() # change to upper
    return '-'.join(text) # add '-' 

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



# Double Letters
# Get a string from the user, print out another string, doubling every letter.

"""Solution 1"""
"""
Create list
Make new string, double every letter in first string that 
made into list, and then join to convert back into a string
"""
# def double_letters(word):
#     word = list(word) 
#     word2 = "".join([letter * 2 for letter in word])
#     return word2

"""Solution 2"""
"""
Basically does what first solution does
Double letters in first string
Join back into new string
"""
def double_letters(word): 
    dbl_string = [letters * 2 for letters in word] 
    letters = "".join(dbl_string)
    return letters


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

"""Solution 1"""
# def count_letter(letter, word):
#     count = 0 # create count to hold how many
#     for letters in word: # if letter is in word count it
#         if letters == letter: 
#             count = count + 1
#     return count

"""Solution 2"""
"""
Less code, a little quicker
Use .count() to count how many of the letter are in the word
"""
def count_letter(letter, word):
    counting = word.count(letter) 
    return counting

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
  last = sorted(word) # sort into alphabetical order
  return last[-1] # take last letter, which is latest in alphabet

def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    counting_hi = text.count('hi') # use count to count how many times 'hi' is in text
    return counting_hi

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case 
# (all lowercase, underscores for spaces, no special characters).
import string 

def snake_case(text):

    for punc in text:
            if punc in string.punctuation:
                text = text.replace(punc, "")
    text = text.lower()
    text = text.replace(" ", "_")
    return (text)
 

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case 
# (no spaces, no special characters, leading capitals except the first).

"""Solution 1"""
# def camel_case(text):
#     for punc in text:
#         if punc in string.punctuation:
#             text = text.replace(punc, "")
#     text = text.title().replace(" ", "")
#     text = text[0].lower(), text[1:]
#     text = ''.join(text)
#     return text


"""Solution 2"""
"""Cleaned up Solution 1 a little"""
import string
def camel_case(text):
    for punc in text:
        if punc in string.punctuation:
            text = text.replace(punc, "")
    text = text.title().replace(" ", "")
    text = ''.join([text[0].lower(), text[1:]])
    return text


def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    converted = ""
    odd = True
    for letter in text:
        if letter == ' ': 
            odd == True   
        if odd:
            converted += letter.upper()
        else:
            converted += letter.lower()
        odd = not odd
    return(converted)  


def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    # assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPle.' # Should this end with capital E?
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'