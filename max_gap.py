def max_gap(numbers):
    diff_lst = []
    numbers.sort(reverse=True)
    next = 1
    print(numbers)
    while len(numbers):
        diff_lst.append(numbers[0] - numbers[1])
        del numbers[0]
    """ for i in range(len(numbers) + 1):
        diff_lst.append(numbers[i] - numbers[next])
        next += 1 """
    return max(diff_lst)


print(max_gap([13, 3, 5]))
