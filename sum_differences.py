def sum_of_differences(arr):
    result = 0
    arr.sort(reverse=True)
    while len(arr) > 1:
        result += arr[0] - arr[1]
        arr.remove(arr[0])
    return result


print(sum_of_differences([10, 2, 1]))
print(sum_of_differences([1, 1, 1, 1, 1]))
print(sum_of_differences([-17, 17]))
print(sum_of_differences([-1]))
print(sum_of_differences([-3, -2, -1]))
