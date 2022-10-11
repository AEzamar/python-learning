def without_last(lst):
    lst.pop()
    return lst


print(without_last([1, 2, 3, 4, 5]))
print(without_last([9, 7, 6, 9]))
print(without_last([25, 30, 55, 26, 66, 59, 94, 85, 8]))
print(without_last([70, 43, 41, 92]))