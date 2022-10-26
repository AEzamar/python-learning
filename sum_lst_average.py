def sum_average(arr):
    return sum([sum(subArr) for subArr in arr])



print(sum_average([[1, 2, 2, 1], [2, 2, 2, 1]]))