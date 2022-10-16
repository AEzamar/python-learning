def solve(arr):
    positive_lst = sorted(filter(lambda item: item > 0, arr))
    negative_lst = sorted(filter(lambda item: item < 0, arr))
    print(positive_lst)
    print(negative_lst)


print(solve([1, -1, 2, -2, 3]))