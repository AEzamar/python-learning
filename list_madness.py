def array_madness(a, b):
    a_square = [num ** 2 for num in a]
    b_cube = [num ** 3 for num in b]
    print(a_square)
    print(b_cube)


print(array_madness([4, 5, 6], [1, 2, 3]))