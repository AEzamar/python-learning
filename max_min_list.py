import math
def solve(arr):
    arr_copy = arr.copy()
    min_max_arr = []
    while len(sorted(arr_copy, reverse=True)):
        print(math.max(arr_copy))
        arr_copy.pop(0)
    return arr


print(solve([15, 12, 10, 11, 7]))
        
