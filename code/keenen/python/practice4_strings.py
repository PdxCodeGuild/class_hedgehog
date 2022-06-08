

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    text = text.upper()
    text = '-'.join(text)
    return text
    
    ...

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    word = list(word)
    word = ''.join(letter * 2 for letter in word)
    word = str(word)
    return word
    ...

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# # Count Letter
# # Count the number of letter occurances in a string

def count_letter(letter, word):
    counter = 0
    for x in word:
        if x == letter:
            counter += 1
    return counter
    ...

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    last_letter = sorted(word)[-1]
    return last_letter
   

#   ...

def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    hi_count = text.count('hi')
    return hi_count

#   ...

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

# from string import punctuation

import string


def snake_case(text):
    text = text.lower()
    for x in string.punctuation:
        text = text.replace(x, '')
    text = text.replace(' ', '_')
    return text

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    text = text.title().replace(' ', '')
    cc_list = []
    for letter in text:
        if letter not in string.punctuation:
            cc_list.append(letter)
    cc_list[0] = cc_list[0].lower()
    cc_list = ''.join(cc_list)
    return cc_list

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    # alt_case = ''
    # for index, value in enumerate(text):
    #     if index % 2:
    #         alt_case += value.lower()
    #     else:
    #         alt_case += value.upper()
    # return alt_case
    
    text = text.lower()
    alt_case = []
    for x in range (len(text)):
        if x % 2 == 0:
            alt_case.append(text[x].upper())
        else:
            alt_case.append(text[x].lower())
    print(alt_case)
    alt_text = ''.join(alt_case)
    print(alt_text)
    return alt_text
    

    
def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'
