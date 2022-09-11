import functools


def digital_root(n):
    total = 0
    n_list = str(n).split()
    root = functools.reduce(lambda accu, curr: accu + curr, [n])
    print(root)
    """ for digit in n_list:
        n_list.map(int, digit) """

    return root


print(digital_root(123456))