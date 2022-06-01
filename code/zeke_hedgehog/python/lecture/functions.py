





# def greeting(user_name):
#     print(f"Hello {name}")
#     return f"Hello {name}"

# name = input("please enter a name:  ")
# output = greeting(name)
# print("output: ", output)


# output = greeting(name)
# print("output: ", output)


# output = greeting(name)
# print("output: ", output)


# names =  [ "Brock", "Ash", "Misty"]
# for name in names:
#     message = greeting(name)
#     print(message)

# --------------------------------------------
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False 

# number = int(input("Enter a number"))
# if is_even(number):
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")
#--------------------------------------------

# Multiple parameter functions/ positional arguments


def addition(num1, num2):
    result = num1 + num2
    return result   

addition(3,4)

total = addition(1,2)
print(total)

def subtraction(num1, num2):
    result = num1 - num2
    return result   

print(subtraction(3,4))

def return_two():
    return True, False

#----------------------------------
## recursion function

def get_user_input():
    choices = ["rock", "paper", "scissors"]
    user_input = ["Choose rock, paper, or scissors"]
    if user_input in choices:
        return user_input
    else:
        return get_user_input()

print(get_user_input())