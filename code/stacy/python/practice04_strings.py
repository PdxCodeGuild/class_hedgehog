

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    text = text.upper()
    text_list = []
    for letter in text:
        text_list.append(letter)
    text = '-'.join(text_list)
    return text

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    letter_list = []
    for letter in word:
        letter_list.append(letter)
        letter_list.append(letter)        
    word = ''.join(letter_list)
    return word

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    letter_count = 0
    for item in word:
        if item == letter:
            letter_count += 1
    return letter_count

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    latest_letter = 'a'
    for letter in word:
        if alphabet.index(letter) > alphabet.index(latest_letter):
            latest_letter = letter
    return latest_letter

def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    count = text.count('hi')
    return count

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    import string
    text = text.lower()
    valid_characters = []
    for letter in text:
        if letter not in string.punctuation:
            valid_characters.append(letter)
    text = ''.join(valid_characters)
    text_list = text.split()
    snake_text = '_'.join(text_list)
    return snake_text

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    import string
    text = text.title().replace(' ','')
    valid_characters = []
    for letter in text:
        if letter not in string.punctuation:
            valid_characters.append(letter)
    valid_characters[0] = valid_characters[0].lower()
    camel_text = ''.join(valid_characters)
    return camel_text

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    text = text.lower()
    mocking_list = []
    index = 0
    for letter in text:
        if not index % 2:
            mocking_list.append(letter.upper())
        else:
            mocking_list.append(letter)
        index += 1
    mocking_text = ''.join(mocking_list)
    return mocking_text

def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'