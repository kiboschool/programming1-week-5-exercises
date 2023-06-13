# Write a function that returns the smallest item in a list of numbers.

def smallest_list_item(nums):
    smallest = nums[0]
    for item in nums:
        if item < smallest:
            smallest = item
    return smallest

# Tests
print(smallest_list_item([1,2,3,4,5])) # should print 1
print(smallest_list_item([10,20,3,40,50])) # should print 3
