def solve(arr):
    max_arr = sorted(arr, reverse=True)
    min_arr = sorted(arr)
    max_min_arr = []
    for i in range(len(arr)):
        max_min_arr.append(max_arr[i])
        max_min_arr.append(min_arr[i])
        if len(max_min_arr) == len(arr): 
            break
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
