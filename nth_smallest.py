def nth_smallest(arr, pos):
    #return [arr[i] for i in range(len(arr)) if arr[i + 1] == arr[pos]]
    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr)):
        #print('Index of 1',sorted_arr[i + 1])
        if sorted_arr[i + 1] == sorted_arr[pos]:
            return sorted_arr[i]
    #print(sorted_arr[pos])
    #return [i + 1 for i in range(len(sorted(arr)))]


print(nth_smallest([3,1,2], 2))
print(nth_smallest([15,20,7,10,4,3], 3))