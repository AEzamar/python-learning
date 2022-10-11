def without_last(lst):
    lst_copy = lst.copy()
    lst_copy.pop(-1)
    return lst_copy


print(without_last([1, 2, 3, 4, 5]))
print(without_last([9, 7, 6, 9]))
print(without_last([25, 30, 55, 26, 66, 59, 94, 85, 8]))
print(without_last([70, 43, 41, 92]))


#User submitted solution
#Come on!
""" def without_last(lst):
    return lst[:-1] """