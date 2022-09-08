def sum_of_differences(arr):
    result = 0
    next = 1
    arr.sort(reverse=True)
    while len(arr) > 1:
        result += arr[0] - arr[next]
        print(result)
        arr.remove(arr[0])
    return result


print(sum_of_differences([10, 2, 1]))
