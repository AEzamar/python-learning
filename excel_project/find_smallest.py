def find_smallest(numbers, to_return):
    return min(numbers) if to_return.lower() == 'value' else numbers.index(min(numbers))


print(find_smallest([4, 2, -1, 3, 5, 1], 'Value'))
print(find_smallest([4, 2, -1, -3, 5, 1], 'Index'))
