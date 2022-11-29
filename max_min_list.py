def solve(arr):
    max_arr = sorted(arr)
    min_arr = sorted(arr)
    copy_arr = sorted(arr)
    max_min_arr = []
    while len(copy_arr):
        max_min_arr.append(max(max_arr))
        max_arr.pop()
        max_min_arr.append(min(min_arr))
        min_arr.pop(0)
        copy_arr.pop()
        if len(max_min_arr) >= len(arr): return max_min_arr
    return max_min_arr


print(solve([15, 12, 10, 11, 7]))
 

def solve1(arr):
    return [max(arr) and min(arr) for item in arr]


print(solve1([15, 12, 10, 11, 7]))