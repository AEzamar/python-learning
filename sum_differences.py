def sum_of_differences(arr):
    result = 0
    curr = 0
    next = 1
    arr.sort(reverse=True)
    print(arr)
    while len(arr):
        result += arr[curr] - arr[next]
        arr.pop()
    return result


print(sum_of_differences([10, 2, 1]))