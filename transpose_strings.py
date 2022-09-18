def transpose_two_strings(arr):
    transposed = ""
    transposed += [(char, chaar) for char, chaar in (arr[0], arr[1])]
    """ for char in arr[0]:
        transposed += f"{char}\n" """
    return transposed.rstrip()


print(transpose_two_strings(['Hello', 'World']))

#[(title, year) for (title, year) in movies if year >= 2000]