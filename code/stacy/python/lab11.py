import string

''' Version 1 '''

# def rot_13_mkI(input_string):
#     lower_alphabet = string.ascii_lowercase
#     output_string = ''
#     for index, letter in enumerate(input_string):
#         output_string+= ''.join(lower_alphabet[(index + 13)%26])
#     return output_string

''' Version 2 '''

def rot_mkII(input_string:str, rot_x: int):
    lower_alphabet = string.ascii_lowercase
    output_string = ''
    for index, letter in enumerate(input_string):
        output_string+= ''.join(lower_alphabet[(index + rot_x)%26])
    return output_string

''' Version 3 '''

def main():
    rot_x = int(input("Enter rotational factor for ROT cypher (must be an integer): \n\t: ").replace(' ',''))
    user_input = (rot_mkII(input("Enter letters to be encrypted with ROT13 cypher: \n\t> "), rot_x))
    print(user_input)

main()


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