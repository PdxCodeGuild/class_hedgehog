import math
# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy
# level and weather


def go_hiking(energy_level, weather):
    # solution 1
    # return energy_level == "spry" and weather == "sunny"

    # solution 2
    # if "rainy" in weather:
    #     return False
    # if "spry" in energy_level:
    #     return True
    # return False

    # solution 3
    if "rainy" in weather or "tired" in energy_level:
        return False
    return True


def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True


# Double Digit
# Write a function that returns True if the number is a
# double digit

def double_digit(num):
    # solution 1
    # return len(str(abs(num))) == 2

    # solution 2
    # if num > 9 and num < 100:  # 9 < num < 100
    #     return True
    # elif num < -9 and num > -100:  # -9 > num > -100
    #     return True
    # return False

    # solution 3
    # num = str(num)
    # num = num.replace("-", "")
    # return len(num) == 2

    # solution 4
    if num in range(10, 100) or num in range(-99, -9):
        return True
    return False


def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`,
# and returns `True` if one is positive and the other is negative,
# and return `False` otherwise.

def opposite(a, b):
    # solution 1
    # return a * b < 0

    # solution 2
    # if a < 0 and b > 0:
    #     return True
    # elif a > 0 and b < 0:
    #     return True

    # return False

    # solution 3
    # return not str(a * b).isdigit()

    # solution 4
    return (a != abs(a) or b != (abs(b))) and (a == abs(a) or b == (abs(b)))


def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False


# Near 100
# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    # solution 1
    # return 90 <= num <= 110

    # solution 2
    # if num in range(90, 111):
    #     return True
    # return False

    # solution 3
    return abs(100 - num) <= 10


def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False
