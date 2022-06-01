# user_input = input("Enter a number: ")


""" except multiple errors """
# try:
#     num = int(user_input)
#     num / 0
# except ValueError:
#     num = 0
# except ZeroDivisionError:
#     print("You can not divide by zero")

""" except multiple errors using a tuple """
# try:
#     num = int(user_input)
#     num / 0
# except (ValueError, ZeroDivisionError):
#     num = 0


""" excepts all errors, not best practice """
# try:
#     num = int(user_input)
#         print("Hello")
# except:
#     num = 0

# cookies = ["chocolate chip", "sugar", "oatmeal", "ginger"]
# try:
#     for i in range(5):
#         print(cookies[i])
# except IndexError:
#     print("Ran out of cookies... :(")

nums = []

""" User input example """
# while True:
#     try:
#         num = input("Enter a number, or 'done' to quit: ")
#         nums.append(int(num))
#     except ValueError:
#         if(num == "done"):
#             break
#         print(f"{num} is not a number, try again.")

""" else and finally example """
# while True:
#     try:
#         num = input("Enter a number, or 'done' to quit: ")
#         nums.append(int(num))
#     except ValueError:
#         break
#     else:   # If no exception is thrown, run else statement
#         print(f"Adding {num} to list...")
#     finally:  # finally will run each time
#         print(nums)


""" raise error"""
# def sum(num1, num2):
#     if(type(num1) != int or type(num2) != int):
#         4 / 0
#         raise ValueError(f"num1: {num1} and num2: {num2} must be integers")

#     return num1 + num2


# print(sum(3, "panda"))

""" Recreate python sum function """
# def better_sum(*args):
#     total = 0
#     for arg in args:
#         if type(arg) != int:
#             raise TypeError(f"{arg} must be of type int")
#         total += arg

#     return total


# result = better_sum(2, 3, 4, 5, 6, 5)
# print(result)
