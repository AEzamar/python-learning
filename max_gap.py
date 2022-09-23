def max_gap(numbers):
    numbers_copy = numbers[:]
    diff_lst = []
    numbers_copy.sort(reverse=True)
    while len(numbers_copy):
        diff_lst.append(numbers_copy[0] - numbers_copy[1])
        del numbers_copy[0]
        if len(numbers_copy) == 1:
            break
    return max(diff_lst)


print(max_gap([13, 3, 5]))
print(max_gap([13,10,2,9,5]))
print(max_gap([24,299,131,14,26,25]))


#User submitted solutions
""" def max_gap(numbers):
    lst = sorted(numbers)
    return max(b-a for a,b in zip(lst, lst[1:])) """


""" import numpy
def max_gap(numbers):
    return max(numpy.diff(sorted(numbers))) """