from colorama import Fore, Back, Style

# print("Hello World")
# prints output of "Hello World" in terminal

# string, surrounded by quotes
# "This is a string"
# 'Is this a string?'
# "This is 'also' a string!"

# be consistent with your ""

# Integer, whole number
5       # int
"5"     # str
5.0     # float
["tomato", 4, 2.3]      # list
True    # boolean
False   # boolean
None    # none 

# dictionary
{"apple": "red", "pumpkin": "orange"}     

("Hello", "World") # tuple / immutable .. can not change

# variable
statement = "conditional statement"

# if statement
# if statement:
    # print("condition was true") # prints if True
# elif not statement: 
    # print("What is happening?")  # prints if False
# else:
    # print("Not true") # prints if False if no other statements are True

# variables are mutable

greeting = "Hello"
greeting = greeting.upper()   #reassigns it as uppercase

# print("Hello".upper())  # prints uppercase hello

colors = ["red", "green", "blue"]

colors[0] = "purple"   #reassigns position 0 to purple

colors.append("orange") # adds "orange" to list

# print(colors)

# immutable datatypes
# tuples
# ints
# floats
# strings
# booleans
# None

# Mutalbe datatypes
# list
# dictionaries 

# commas separate items
# sep= separates items using whatever you want
# end= changes what happens at end of the print statment

# input is for user inputs
# inputs are always strings
# oper_sys = input("Enter your OS: ")
# print (oper_sys + ' is the best OS!')

# age = input("Enter your age: ")
# print(f"Happy birthday you are {int(age) + 1}!")

# typecasting 
# int() - changes to an integer
# str() - changes to a string
# float() - changes to a float
# bool() - changes to a True

print(Fore.RED + "some red text")
print(Back.BLUE + "blue background text")
print(Style.RESET_ALL)



