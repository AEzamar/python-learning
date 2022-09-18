def transpose_two_strings(arr):
    i = 0
    transposed = ""
    for char in zip(arr[0], arr[1]):
        transposed += str(char)
    return transposed


print(transpose_two_strings(['Hello', 'World']))