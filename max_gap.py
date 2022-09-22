def max_gap(numbers):
    diff_lst = []
    numbers.sort(reverse=True)
    next = 1
    print(numbers)
    """ for i in range(len(numbers) + 1):
        diff_lst.append(numbers[i] - numbers[next])
        next += 1 """
    return diff_lst


print(max_gap([13, 3, 5]))
