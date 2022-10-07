def nth_smallest(arr, pos):
    #sorted_arr = sorted(arr)
    return [arr[i] for i in range(len(sorted(arr))) if arr[i + 1] == arr[pos]]
    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr) + 1):
        #print('Index of 1',sorted_arr[i + 1])
        if sorted_arr[i + 1] == sorted_arr[pos]:
            return sorted_arr[i]


print(nth_smallest([3,1,2], 2))
print(nth_smallest([15,20,7,10,4,3], 3))