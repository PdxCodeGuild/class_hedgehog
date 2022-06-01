
# def greeting(name):
#     print(f"Hello {name}")

#     return f"{name} is a pokemon master!"


# name = input("Please enter your name: ")
# output = greeting(name)
# print("Output: ", output)

# output = greeting("Joe")
# print("Output: ", output)

# output = greeting("Susan")
# print("Output: ", output)

# names = ["Brock", "Ash", "Misty", "Team Rocket", "Gary"]
# for name in names:
#     message = greeting(name)
#     print(message)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# number = int(input("Enter a number"))
# if is_even(number):
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


def addition(num1, num2):
    result = num1 + num2
    return result


def subtraction(num1, num2=0, num3=0, num4=0):
    result = num1 - num2 - num3 - num4
    return result


def say_hi():
    """ will return None """
    hello = "hello world"


# goodbye = say_hi()  # None
# print(goodbye)


def return_two():
    return "Hello World", ["red", "green", "blue"]


message = return_two()
# print(message)
# print(rgb)


def recursion():
    """recursive function"""
    return recursion()


# print(type(recursion()))

def get_user_input():
    choices = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, or scissors: ")
    if user_input in choices:
        return user_input
    else:
        return get_user_input()


# print(get_user_input())

"""lamda or unnamed function"""
def sum(num1, num2): return num1 + num2


print(sum(1, 2))
