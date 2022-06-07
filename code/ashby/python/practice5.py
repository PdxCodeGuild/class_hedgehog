# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"




# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def even_even(nums):
    # count = [x for x in nums if x%2==0]
    # return len(count)%2==0
    count = 0
    for x in nums:
        if x%2==0:
            count +=1
    if count == 0:
        return "No evens"
    elif count%2 == 0:
        return True
    else:
        return False


def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


## Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    return nums[::-1]
    ...

def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]



# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
  return [x for x in nums1 if x in nums2]

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    super_nums = []
    for x in range(len(nums1)):
        super_nums.append(nums1[x])
        super_nums.append(nums2[x])
    return super_nums

    ...
    
def test_combine():
    assert combine(['a','b','c'],[1,2,3]) == ['a', 1, 'b', 2, 'c', 3]



# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    answers = []
    for num in nums:
        for x in range(len(nums)):
            if num == nums[x]:
                pass
            elif num + nums[x] == target:
                answers.append(num)
                answers.append(nums[x])
                return answers


def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]




# Average
# Write a function to find the average of a list of numbers


def average(nums):
    return int(sum(nums)/len(nums))
def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    for x in mylist:
        mylist.remove("")
    return mylist

def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']



# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    merge_list = []
    for x in range(len(nums1)):
        merge_list.append([nums1[x],nums2[x]])
    return merge_list
    
def test_merge():
    assert merge([5,2,1], [6,8,2]) == [[5,6],[2,8],[1,2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    combine_list = []
    for num in nums:
        for x in num:
            combine_list.append(x)
    return combine_list
    
def test_combine_all():
    assert combine_all([[5,2,3],[4,5,1],[7,6,3]]) == [5,2,3,4,5,1,7,6,3]