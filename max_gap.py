def max_gap(numbers):
    numbers_copy = numbers[:]
    diff_lst = []
    numbers_copy.sort(reverse=True)
    diff = numbers_copy[0] - numbers_copy[1]
    while len(numbers_copy):
        diff_lst.append(diff)
        del numbers_copy[0]
    return max(diff_lst)


print(max_gap([13, 3, 5]))
