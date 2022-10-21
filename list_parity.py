def solve_long(arr):
    positive_lst = sorted(filter(lambda item: item > 0, arr))
    negative_lst = sorted(filter(lambda item: item < 0, arr))
    for i in range(len(arr)):
        if len(positive_lst) > len(negative_lst):
            if -abs(positive_lst[i]) not in negative_lst:
                return positive_lst[i]
        if len(negative_lst) > len(positive_lst):
            if abs(negative_lst[i]) not in positive_lst:
                return negative_lst[i]


""" print(solve_long([1, -1, 2, -2, 3]))
print(solve_long([1, 3, 2, -1, -3]))
print(solve_long([-3, 1, 2, 3, -1, -4, -2]))
print(solve_long([1, -1, 2, -2, 3, 3])) """


def find_item(func, arr):
    for item in arr:
        if func(item): return item


def solve(arr):
    return find_item(lambda item: -abs(item) not in arr or abs(item) not in arr, arr)


print(solve([1, -1, 2, -2, 3]))
print(solve([1, 3, 2, -1, -3]))
print(solve([-3, 1, 2, 3, -1, -4, -2]))
print(solve([1, -1, 2, -2, 3, 3]))