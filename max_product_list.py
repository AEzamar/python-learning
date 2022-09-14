import functools
def max_product(lst, n_largest_elements):
    sub_lst = lst[0 : n_largest_elements]
    functools.reduce(lambda a, b: a * b, lst[range(n_largest_elements)])
