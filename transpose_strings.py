def transpose_two_strings(arr):
    i = 0
    transposed = ""
    for char, ch in arr[0], arr[1]:
        transposed += char, ch
    return transposed


print(transpose_two_strings(['Hello', 'World']))