def sum_of_differences(arr):
    result = 0
    curr = 0
    next = 1
    descending = arr.sort(reverse=True)
    print(descending)
    """ while len(arr):
        result += arr[curr] - arr[next]
        arr.pop()
        curr += 1
        next += 1 """
    return result


print(sum_of_differences([10, 2, 1]))