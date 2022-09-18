def transpose_two_strings(arr):
    i = 0
    transposed = ""
    for char in zip(arr[0], arr[1]):
        transposed += str(char) + '\n'
    return transposed.rstrip()


print(transpose_two_strings(['Hello', 'World']))