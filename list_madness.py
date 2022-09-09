def array_madness(a, b):
    if [num ** 2 for num in a] > [num ** 3 for num in b]:
        return True
    else:
        return False