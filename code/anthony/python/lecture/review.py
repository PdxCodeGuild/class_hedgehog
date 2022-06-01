from colorama import Fore, Back, Style

# print("Class Hedgehog")

# String, surrounded by quotes
# "This is a string"
'Is this "a" string?'
"This is 'also' a string"

# Integer, whole number
5       # int
"5"     # str
5.0     # float
["tomato", 4, 2.3]      # list
True    # boolean
None    # none
{}      # dictionary
{"apple": "red", "pumpkin": "orange"}

("Hello", "World")  # Tuple / immutable.. can not change

statement = 3 > 4
# if statement
# if statement:
#     print("Condition was true")
# elif not statement:
#     print("What is happening?")
# else:
#     print("Not true")


greeting = "Hello"
greeting = greeting.upper()

# print(greeting)

colors = ["red", "green", "blue"]

# print(colors[0])

# colors.append("orange")

# Immutable datatypes
# tuples
# ints
# floats
# strings
# booleans
# None

# Mutable datatypes
# list
# dictionaries


# print("Hello", 4, 7, False, sep="", end="\n\n")
# print("Hi")
# print("Hedgehog")

# operating_system = input("Enter your OS: ")
# print(operating_system + " Is the best OS!")

# age = input("Enter your age (as a number): ")  # 30 + 1

# age = int(age)

# print(f"Happy birthday you are {age + 1}")


price = 4.5
price = bool(price)
# print(price)

message = "Hello World"
message = list(message)

# print(message)
print(Fore.RED + "Some red text")
print(Back.BLUE + "blue background text")

print(Fore.CYAN + Back.WHITE + "Some cool text")
print(Style.RESET_ALL)
print("Something else")
