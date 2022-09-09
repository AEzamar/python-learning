def array_plus_array(arr1, arr2):
    total = 0
    for num in arr1 + arr2:
        total += num
    return total


print(array_plus_array([1, 2, 3], [4, 2, 1]))
print(array_plus_array([9, 3, 11], [22, 14, 10]))