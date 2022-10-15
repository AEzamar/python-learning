def solve(arr):
    iteration_arr = arr.copy()
    max_arr = sorted(arr, reverse=True)
    min_arr = sorted(arr)
    max_min_arr = []
    index = 0
    #for i in range(len(arr)):
    while(len(iteration_arr)):
        max_min_arr.append(max_arr[index])
        max_min_arr.append(min_arr[index])
        index += 1
        del iteration_arr[0]
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
