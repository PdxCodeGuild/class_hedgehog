
# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather

"""Solution 1"""

# energy = ""
# weather = ""

# def go_hiking(energy, weather):
    
#     if energy == "tired" and weather == "rainy":
#         return False
#     elif energy == "spry" and weather == "rainy":
#         return False
#     elif energy == "tired" and weather == "sunny":
#         return False
#     elif energy == "spry" and weather == "sunny":
#         return True

"""Solution 2"""
# def go_hiking(energy, weather):
#     if "tired" in energy:
#         return False 
#     if "rainy" in weather:
#         return False        
#     if "spry" in energy:
#         return True
#     if "sunny" in weather:
#         return True

"""Solution 3"""
def go_hiking(energy, weather):
    if energy == "spry" and weather == "sunny":
        return True
    else:    
        return False            
  

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True


# Double Digit
# Write a function that returns True if the number is a double digit

def double_digit(num):
    if num > 9 and num < 100:
        return True
    elif num < -9 and num > -100:
        return True
    else:
        return False


def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`, 
# and returns `True` if one is positive and the other 
# is negative, and return `False` otherwise.

def opposite(a, b):
    if a > 0 and b < 0:
        return True
    elif a < 0 and b > 0:
        return True
    else:
        return False       


def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False


# Near 100
# Write a function that returns True if a number within 10 of 100.

"""Solution 1"""
# def near_100(num):
#     if num >= 90 and num <= 110:
#         return True
#     else:
#         return False    

"""Solution 2"""
def near_100(num):
    return num >= 90 and num <= 110

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False