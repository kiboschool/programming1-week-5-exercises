# Write a function that doubles all the elements in a list.

def double_elements(items):
    doubled = []
    for item in items:
        doubled.append(item * 2)
    return doubled
