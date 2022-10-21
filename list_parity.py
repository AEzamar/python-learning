def solve(arr):
    positive_lst = sorted(filter(lambda item: item > 0, arr))
    negative_lst = sorted(filter(lambda item: item < 0, arr))
    for i in range(len(arr)):
        if len(positive_lst) > len(negative_lst):
            if -abs(positive_lst[i]) not in negative_lst:
                return positive_lst[i]
        if len(negative_lst) > len(positive_lst):
            if abs(negative_lst[i]) not in positive_lst:
                return negative_lst[i]


print(solve([1, -1, 2, -2, 3]))
print(solve([1, 3, 2, -1, -3]))
print(solve([-3, 1, 2, 3, -1, -4, -2]))
print(solve([1, -1, 2, -2, 3, 3]))


def find_ele(func, arr):
    return[func(ele) for ele in arr]


def solve1(arr):
    return find_ele(lambda item: item != -abs(item), arr)
    #return list(filter(lambda ele: ele != -abs(ele), arr))
    return [-abs(ele) not in arr for ele in arr]


print('Solve 1:', solve1([1, -1, 2, -2, 3]))