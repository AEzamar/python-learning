def solve(arr):
    arr_copy = arr.copy()
    max_min_arr = []
    while len(sorted(arr_copy, reverse=True)):
        #print(max(arr_copy))
        arr_copy.pop(0)
        """ max_min_arr.append(arr_copy.pop(0))
        max_min_arr.append(arr_copy.pop()) """
        #arr_copy.pop(0)
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
