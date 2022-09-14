import functools
def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    sub_lst = lst[:n_largest_elements]
    print(sub_lst)
    return functools.reduce(lambda a, b: a * b, sub_lst)



print(max_product([4, 3, 5], 2))