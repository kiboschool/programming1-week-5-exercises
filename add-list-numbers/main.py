# Write a function called numbers_sum that calculates the sum of all numbers in a list
def numbers_sum(numbers):
    total = 0  # start from 0
    
    for num in numbers:
        total += num  # add each number to total
    
    return total  # return the final sum

print(numbers_sum(range(1,200)))