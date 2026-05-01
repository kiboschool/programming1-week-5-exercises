# Write a function that returns the smallest item in a list of numbers.
def smallest_list_item(numbers):
    smallest = numbers[0]  # assume first item is smallest

    for num in numbers:
        if num < smallest:
            smallest = num  # update if smaller number is found

    return smallest

print(smallest_list_item([5, 2, 8, 1, 4]))