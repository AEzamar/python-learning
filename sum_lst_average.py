from functools import reduce
def sum_average(arr):
    return sum([sum(subArr) for subArr in arr])


print(sum_average([[1, 2, 2, 1], [2, 2, 2, 1]]))
print(sum_average([[52, 64, 84, 21, 54], [44, 87, 46, 90, 43]]))