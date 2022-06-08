"""
def latest_letter(word): #passes word in
    highest_letter = sorted(word)[-1] #creates sorted list in alphabetic order and selects last item in string
    print(word)
    return highest_letter #returns the lasr letter in the string

print(latest_letter("poqzmry"))
"""
from ntpath import join


mystring = 'Python'
print(reversed(mystring)) # <reversed object at 0x7fb67b77dd68>
print(list(reversed(mystring))) # ['n', 'o', 'h', 't', 'y', 'P']
print(sorted(mystring)) # ['P', 'h', 'n', 'o', 't', 'y']
print(mystring.join(mystring))
