import math
def solve(arr):
    arr_copy = arr.copy()
    min_max_arr = []
    while len(sorted(arr_copy, reverse=True)):
        print(math.max(arr_copy))
        
