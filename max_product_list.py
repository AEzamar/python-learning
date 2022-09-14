from audioop import reverse
import functools
def max_product(lst, n_largest_elements):
    sub_lst = lst[0 : n_largest_elements]
    sub_lst.sort(reverse=True)
    return functools.reduce(lambda a, b: a * b, sub_lst)



print(max_product([4, 3, 5], 2))