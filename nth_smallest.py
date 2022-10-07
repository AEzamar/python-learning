def nth_smallest(arr, pos):
    #return [i for i in range(len(arr)) if arr[i] == arr[pos]]
    for i in range(len(arr)):
        position = arr[i]
        return arr[pos] == arr[position]
    sorted_arr = sorted(arr)
    print(sorted_arr[pos])
    #return [i + 1 for i in range(len(sorted(arr)))]


print(nth_smallest([3,1,2], 2))
print(nth_smallest([15,20,7,10,4,3], 3))