def min_sum(arr):
    total = 0
    arr.sort(reverse=True)
    negative_i = -1
    for i in range(len(arr)):
        total += arr[i] *