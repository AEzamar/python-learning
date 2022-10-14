def solve(arr):
    return [num for num in arr]
    arr_copy = arr.copy()
    arr_copy_two = arr.copy()
    arr_copy_two.sort()
    max_min_arr = []
    #while len(sorted(arr_copy, reverse=True)):
    for i in range(len(sorted(arr_copy, reverse=True))):
        max_min_arr.append(arr_copy[0])
        max_min_arr.append(arr_copy_two[0])
        del arr_copy[0]
        del arr_copy_two[0]
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
        
