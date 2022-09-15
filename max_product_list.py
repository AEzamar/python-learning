import functools
def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    sub_lst = lst[0 : n_largest_elements]
    return functools.reduce(lambda a, b: a * b, sub_lst)


print(max_product([4, 3, 5], 2))


#User submitted solution, using 3 modules
""" from functools import reduce
from operator import mul
from heapq import nlargest

def maxProduct (lst, n):
    return reduce(mul, nlargest(n, lst)) """