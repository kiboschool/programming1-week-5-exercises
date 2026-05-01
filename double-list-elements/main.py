# Write a function that doubles all the elements in a list.
def double_elements(numbers):
    doubled_list = []  # create a new empty list

    for num in numbers:
        doubled_list.append(num * 2)  # double and add to new list

    return doubled_list  # return the new list
print(double_elements(range(1, 50, 2)))