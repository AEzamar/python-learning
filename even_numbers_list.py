def even_numbers(arr, n):
    return list(filter(lambda ele: ele % 2 == 0, arr))[-n:]


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

