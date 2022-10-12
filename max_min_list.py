def solve(arr):
    arr_copy = arr.copy()
    max_min_arr = []
    #while len(sorted(arr_copy, reverse=True)):
    for i in range(len(arr_copy)):
        max_min_arr.append(arr_copy[0])
        max_min_arr.append(arr_copy[-1])
        del arr_copy[0]
        del arr_copy[-1]
        """ max_min_arr.append(arr_copy.pop(0))
        max_min_arr.append(arr_copy.pop()) """
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
