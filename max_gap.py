def max_gap(numbers):
    numbers_copy = numbers[:]
    diff_lst = []
    numbers_copy.sort(reverse=True)
    while len(numbers_copy):
        #diff = numbers_copy[0] - numbers_copy[1]
        #print(numbers_copy)
        diff_lst.append(numbers_copy[0] - numbers_copy[1])
        del numbers_copy[0]
        if len(numbers_copy) == 1:
            break
    """ print(numbers_copy)
    print(diff_lst) """
    return max(diff_lst)


print(max_gap([13, 3, 5]))
print(max_gap([13,10,2,9,5]))
