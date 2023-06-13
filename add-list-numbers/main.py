# Write a function called numbers_sum that calculates the sum of all numbers in a list

def numbers_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Manually testing the solution by printing values
print(numbers_sum([1,2,3])) # should print 6
print(numbers_sum([10,20,30])) # should print 60
