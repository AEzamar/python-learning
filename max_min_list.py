def solve(arr):
    max_arr = sorted(arr, reverse=True)
    min_arr = sorted(arr)
    copy_arr = sorted(arr)
    max_min_arr = []
    i = 0
    #for i in range(len(copy_arr)):
    while len(copy_arr):
        """ max_min_arr.append(max_arr[i])
        max_min_arr.append(min_arr[i]) """
        print(max(arr))
        arr.pop(0)
        print(min(arr))
        arr.pop()
        #max_min_arr.append(arr.remove(max(arr)))
        i += 1
        del copy_arr[0]
        if len(max_min_arr) > len(arr): break
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
