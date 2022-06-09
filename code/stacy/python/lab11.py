import string

''' Version 1 '''

def rot_13_mkI():
    input_string = input('Enter characters to be encripted with ROT13: \n\t> ').lower().replace(' ','')
    lower_alphabet = string.ascii_lowercase
    modified_input_string = ''
    for character in input_string:
        if character in lower_alphabet:
            modified_input_string += ''.join(character)
    output_string = ''
    for letter in modified_input_string:
        output_string+= ''.join(lower_alphabet[(lower_alphabet.index(letter) + 13)%26])
    return output_string

''' Version 2 '''

def rot_mkII():
    rotational_factor = int(input("Enter rotational factor: \n\t> "))
    input_string = input(f'Enter characters to be encripted with rotational factor of {rotational_factor} \n\t> ').lower().replace(' ','')
    lower_alphabet = string.ascii_lowercase
    modified_input_string = ''
    for character in input_string:
        if character in lower_alphabet:
            modified_input_string += ''.join(character)
    output_string = ''
    for letter in modified_input_string:
        output_string+= ''.join(lower_alphabet[(lower_alphabet.index(letter) + rotational_factor)%26])
    return output_string

''' Version 3 '''

def rot_mkIII_rotate_all():
    rotational_factor = int(input("Enter rotational factor: \n\t> "))
    input_string = input(f'Enter characters to be encripted with rotational factor of {rotational_factor} \n\t> ')
    all_valid_characters = string.ascii_letters + string.digits + ' ' + string.punctuation 
    output_string = ''
    for letter in input_string: #index current lett plus rotational factor modulus len of all valid
        output_string += ''.join(all_valid_characters[(all_valid_characters.index(letter) + rotational_factor)%len(all_valid_characters)])
    return output_string

def rot_mkIII_rotate_without_punctuation():
    rotational_factor = int(input("Enter rotational factor: \n\t> "))
    input_string = input(f'Enter characters to be encripted with rotational factor of {rotational_factor} \n\t> ')
    all_letters = string.ascii_letters
    output_string = ''
    for letter in input_string: #index current lett plus rotational factor modulus len of all valid
        if letter in string.punctuation or letter in string.digits:
            output_string += ''.join(letter)
        elif letter == ' ':
            output_string += ''.join(' ')
        elif letter in all_letters:
            output_string += ''.join(all_letters[(all_letters.index(letter) + rotational_factor)%len(all_letters)])
    return output_string

def rot_mkIII_rotate_letters_only():
    rotational_factor = int(input("Enter rotational factor: \n\t> "))
    input_string = input(f'Enter characters to be encripted with rotational factor of {rotational_factor} \n\t> ')
    output_string = ''
    for letter in input_string: #index current lett plus rotational factor modulus len of all valid
        if letter in string.punctuation or letter in string.digits:
            output_string += ''.join(letter)
        elif letter == ' ':
            output_string += ''.join(' ')
        elif letter in string.ascii_lowercase:
            output_string += ''.join(string.ascii_lowercase[(string.ascii_lowercase.index(letter) + rotational_factor)%len(string.ascii_lowercase)])
        elif letter in string.ascii_uppercase:
            output_string += ''.join(string.ascii_uppercase[(string.ascii_uppercase.index(letter) + rotational_factor)%len(string.ascii_uppercase)])
    return output_string

def main():
    print(rot_13_mkI())
    print(rot_mkII())
    print(rot_mkIII_rotate_all())
    print(rot_mkIII_rotate_without_punctuation())
    print(rot_mkIII_rotate_letters_only())
    '''
    Rot Cipher
    Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

    Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
    English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
    ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
    Version 2
    Allow the user to input the amount of rotation used in the encryption. (ROTN)

    Version 3 (optional)
    Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

    Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

    Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.
    '''

main()