# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"




# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.




def even_even(nums):
    even = 0
    for num in nums:
        if not num % 2:
            even += 1
    return not even  % 2

def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False




## Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    rev = nums[::-1]
    return rev

def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]




# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    # solution 1
    return [i for i in nums1 if i in nums2]

    # solution 2
    # new_list = []
    # for i in nums1:
    #     if i in nums2:
    #         new_list.append(i)
    # return new_list
            

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]




# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    return [x for y in zip(nums1, nums2) for x in y]  # discovered zip class which takes first item in each passed iterator(ex. position [0] in nums1 and nums2) and pairs them together and continues in order.
    
def test_combine():
    assert combine(['a','b','c'],[1,2,3]) == ['a', 1, 'b', 2, 'c', 3]






# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.

def find_pair(nums, target):
    ...

def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]





# Average
# Write a function to find the average of a list of numbers

def average(nums):
    return sum(nums) / len(nums)

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3




# Remove Empty
# Write a function to remove all empty strings from a list.

def remove_empty(mylist):
    for i in mylist:
        if i == '':
            mylist.remove(i)
    return mylist


def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']




# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
from itertools import chain

def merge(nums1, nums2):
    ...
    
def test_merge():
    assert merge([5,2,1], [6,8,2]) == [[5,6],[2,8],[1,2]]




# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.

def combine_all(nums):
    num_list = []
    for i in range(len(nums)):
        for x in range(len(nums[i])):
            num_list.append(nums[i][x])
    return num_list
    
def test_combine_all():
    assert combine_all([[5,2,3],[4,5,1],[7,6,3]]) == [5,2,3,4,5,1,7,6,3]