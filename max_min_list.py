def solve(arr):
    max_arr = sorted(arr, reverse=True)
    min_arr = sorted(arr)
    copy_arr = sorted(arr, reverse=True)
    max_min_arr = []
    #for i in range(len(arr)):
        if max_arr[i] and min_arr[i] not in max_min_arr:
            max_min_arr.append(copy_arr[i])
            del copy_arr[0]
            max_min_arr.append(copy_arr[-i])
            del copy_arr[-1]
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
