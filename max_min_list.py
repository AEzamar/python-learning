def solve(arr):
    max_arr = sorted(arr, reverse=True)
    min_arr = sorted(arr)
    max_min_arr = []
    for i in range(len(arr)):
        max_min_arr += max_arr[i]
        max_min_arr += min_arr[i]
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
