def min_sum(arr):
    total = 0
    arr.sort(reverse=True)
    while len(arr):
         total += arr[0] * arr[-1]
         del arr[0]
         arr.pop()
    return total


print(min_sum([12, 6, 10, 26, 3, 24]))
print(min_sum([5,4,2,3]))
print(min_sum([9,2,8,7,5,4,0,6]))