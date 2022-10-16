def solve(arr):
    negative_lst = filter(lambda item: item > 0, arr)
    positive_lst = filter(lambda item: item < 0, arr)