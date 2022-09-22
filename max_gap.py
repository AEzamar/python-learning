def max_gap(numbers):
    diff_lst = []
    numbers.sort(reverse=True)
    diff = numbers[0] - numbers[1]
    while len(numbers):
        diff_lst.append(diff)
        del numbers[0]
    return max(diff_lst)


print(max_gap([13, 3, 5]))
