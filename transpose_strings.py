def transpose_two_strings(arr):
    transposed = ""
    for char in zip(arr[0], arr[1]):
        transposed += str(char) + '\n'
    return transposed.rstrip()


print(transpose_two_strings(['Hello', 'World']))

#[(title, year) for (title, year) in movies if year >= 2000]