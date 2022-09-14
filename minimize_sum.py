def min_sum(arr):
    total = 0
    arr.sort(reverse=True)
    while len(arr):
         total += arr[0] * arr[-1]
         del arr[0]
         arr.pop()
    return total


print(min_sum([12, 6, 10, 26, 3, 24]))