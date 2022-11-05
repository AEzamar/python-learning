def solve(arr):
    max_arr = sorted(arr)
    min_arr = sorted(arr)
    copy_arr = sorted(arr)
    copy_arr_2 = sorted(arr)
    max_min_arr = []
    while len(copy_arr):
        """ max_min_arr.append(max(max_arr))
        max_arr.pop()
        max_min_arr.append(min(min_arr))
        min_arr.pop(0)
        del copy_arr[0] """
        max_min_arr.append(max(copy_arr))
        max_min_arr.append(min(copy_arr_2))
        copy_arr.pop()
        copy_arr_2.pop(0)
        if len(copy_arr) == 1:
            max_min_arr.append(copy_arr.pop())
        if len(copy_arr_2) == 1:
            max_min_arr.append(copy_arr_2.pop())
        #if len(max_min_arr) >= len(arr): return max_min_arr
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
