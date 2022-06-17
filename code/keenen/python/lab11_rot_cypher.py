
# """ Version 1 """

# def main():

#     rot_13 = {
#         'a': 'n',
#         'b': 'o',
#         'c': 'p',
#         'd': 'q',
#         'e': 'r',
#         'f': 's',
#         'g': 't',
#         'h': 'u',
#         'i': 'v',
#         'j': 'w',
#         'k': 'x',
#         'l': 'y',
#         'm': 'z',
#         'n': 'a',
#         'o': 'b',
#         'p': 'c',
#         'q': 'd',
#         'r': 'e',
#         's': 'f',
#         't': 'g',
#         'u': 'h',
#         'v': 'i',
#         'w': 'j',
#         'x': 'k',
#         'y': 'l',
#         'z': 'm',
#         ' ': ' '
#         }
#     # print(rot_13)

#     user_list = []

#     user = input('\nEnter the alphabetical characters you would like to encrypt/rotate: ').lower()
#     # print(user)

#     user_list.append(user)
#     # # print(user_list)
#     user_list = ''.join(user_list)
#     # # print(user_list)
#     user_list = list(user_list)
#     # print(user_list)
    
#     output = ''

#     for i in range(len(user_list)):
#         if any(user_list[i] in keys for keys in rot_13):
#             output += rot_13.get(user_list[i])
#             
#     print(f'\nYour encrypted/rotated characters are: {output}\n')
    
# main()
        

        
""" Version 2 """

import string

def rot():

    rot_list = list(string.ascii_lowercase)
    rotated = ''
    # print(rot_list)
    user = input('\nEnter the alphabetical characters you would like to encrypt/rotate: ').lower()
    rotations = int(input('\nHow many rotations would you like to perform on each character you enter: '))

    for character in user:
        if character in rot_list:
            index = (rot_list.index(character) + rotations) % 26
            # print(index)
            rotated += rot_list[index]
            # print(rotated)
        else:
            rotated += character

    print(f'\nThe encrypted version of the characters you entered is: {rotated}')


rot()
    
    
    
    
    
    
    
    
    # list_keys = list(rot_user.keys())
    # list_values = list(rot_user.values())
    
    # print(list_keys)
    # print(list_values)
    # output = ''

    # while counter > 26:
    #     counter -= 26
    # # print(counter)

    # for i in list_values:
    #     # print(rot_user.keys())
    #     while user == list_values.index(user):
    #         print(list_values[i])

    #     output = rot_user[(rotations) + counter]
    # print(output)
    
    # for i, v in enumerate(rot_user):
    #     output = (i + counter) % 26
    # # print(output)
    # for output in rot_user.keys():
    #     print((rot_user.keys()))