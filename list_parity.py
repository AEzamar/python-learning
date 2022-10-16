def solve(arr):
    positive_lst = sorted(filter(lambda item: item > 0, arr))
    negative_lst = sorted(filter(lambda item: item < 0, arr))
    for i in range(len(arr)):
        if -int(positive_lst[i]) not in negative_lst:
            return positive_lst[i]

print(solve([1, -1, 2, -2, 3]))