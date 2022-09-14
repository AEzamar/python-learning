def min_sum(arr):
    total = 0
    arr.sort(reverse=True)
    minus_i = -1
    for i in range(len(arr)):
        total += arr[i] * arr[minus_i]
        minus_i += -1
    return total


print(min_sum([12, 6, 10, 26, 3, 24]))