

# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns
# a new list with every number doubled

def double_numbers(nums):

    # solution 1
    # for i in range(len(nums)):
    #     nums[i] *= 2
    # return nums

    # solution 2
    # return [num*2 for num in nums]

    # solution 3
    # doubled = []
    # for num in nums:
    #     doubled.append(num * 2)
    # return doubled

    # solution 4
    return list(map(lambda num: num*2, nums))


def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


# Stars
# Write a function that takes an integer and returns
# that number of asterisks in a string

def stars(n):
    # solution 1
    # return "*" * n

    # solution 2
    # star = n * "*"
    # return star

    # solution 3
    # star = ""
    # for x in range(n):
    #     star += "*"

    # return star

    # solution 4
    # if n == 1:
    #     return "*"
    # return f"*{stars(n-1)}"

    # solution 5
    return "".join(["*" for x in range(n)])


def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a
# list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):

    # solution 1
    # nums2 = []
    # for num in nums:
    #     if num < 10:
    #         nums2.append(num)
    # return nums2

    # solution 2
    # return [x for x in nums if x < 10]

    # solution 3
    nums2 = []
    i = 0
    while i < len(nums) - 1:
        if nums[i] < 10:
            nums2.append(nums.pop(i))
        else:
            i += 1

    return nums2


def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]
