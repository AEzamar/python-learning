def solve(arr):
    positive_lst = sorted(filter(lambda item: item > 0, arr))
    negative_lst = sorted(filter(lambda item: item < 0, arr))
    for i in range(len(arr)):
        if -abs(positive_lst[i]) not in negative_lst or abs(negative_lst[i]) not in positive_lst:
            return positive_lst[i] or negative_lst[i]


""" print(solve([1, -1, 2, -2, 3]))
print(solve([1, 3, 2, -1, -3]))
print(solve([-3, 1, 2, 3, -1, -4, -2])) """

def solve1(arr):
    return [-abs(ele) not in arr for ele in arr]


print(solve1([1, -1, 2, -2, 3]))