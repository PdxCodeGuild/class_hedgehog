
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
        

counter = 0
rotations = int(input('How many rotations would you like to perform on each character you enter: '))
counter += rotations

while counter > 26:
    counter -= 26


print(counter)
