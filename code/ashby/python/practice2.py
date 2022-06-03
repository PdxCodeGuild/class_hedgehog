# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather
"""Very specific, but I guess if it fits the bill it pays"""

from cmath import sqrt


def go_hiking(energy, weather):
    return energy == "spry" and weather == "sunny"

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True


# Double Digit
# Write a function that returns True if the number is a double digit


def double_digit(num):
    """Solution 3, because what if abs wasn't a function and I hated myself. Also, produces a complex so not a good idea."""
    #return sqrt(num**2) in range(10,99)

    """Solution 2, slightly cleaner"""
    return abs(num)in range(10,99)
    
    """Solution 1, kinda gross"""
    #return num in range(10,99) or num in range(-99,-10)

def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.
"""Pretty pleased with this one. Simple and to the point"""

def opposite(a, b):
    if a == 0 or b ==0:
        return "I refuse to get caught up in this philosophical discussion, please do not use zero in the future."
    return a*b < 0
    ...

def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False


# Near 100
# Write a function that returns True if a number within 10 of 100.

"""Again, very specific, but thems the brakes"""
def near_100(num):
    return num in range(90,110)
    
    #Alternate solution
    #return num >= 90  and num <= 110

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False