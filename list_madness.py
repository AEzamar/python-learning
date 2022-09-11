import functools


def array_madness(a, b):
    a_square = [num ** 2 for num in a]
    b_cube = [num ** 3 for num in b]
    for i in range(len(a_square)):
        if a_square[i] > b_cube[i]:
            return True
        else:
            return False
    """ print(a_square)
    print(b_cube) """


print(array_madness([4, 5, 6], [1, 2, 3]))
print(array_madness([2, 3, 4], [1, 2, 3]))