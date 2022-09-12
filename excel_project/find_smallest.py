def find_smallest(numbers, to_return):
    if to_return.lower() == 'value':
        return min(numbers)
    elif to_return.lower() == 'index':
        return numbers.index(min(numbers))


print(find_smallest([4, 2, -1, 3, 5, 1], 'Value'))
print(find_smallest([4, 2, -1, -3, 5, 1], 'Index'))
