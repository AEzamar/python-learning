import functools


def array_madness(a, b):
    a_square = functools.reduce(lambda accu, curr: accu + curr, [num ** 2 for num in a])
    b_cube = functools.reduce(lambda accu, curr: accu + curr, [num ** 3 for num in b])
    return True if a_square > b_cube else False


print(array_madness([4, 5, 6], [1, 2, 3]))
print(array_madness([2, 3, 4], [1, 2, 3]))


#This is a one line solution submitted by another coder
#I need to start using sum more
""" def array_madness(a,b):
    return sum(x ** 2 for x in a) > sum(x **3 for x in b) """