def solve(arr):
    max_arr = sorted(arr, reverse=True)
    min_arr = sorted(arr)
    copy_arr = sorted(arr)
    max_min_arr = []
    while len(copy_arr):
        max_min_arr.append(max(arr))
        arr.pop(0)
        max_min_arr.append(min(min_arr))
        del min_arr[0]
        del copy_arr[0]
        if len(max_min_arr) >= len(arr): break
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
