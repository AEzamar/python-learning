def transpose_two_strings(arr):
    i = 0
    transposed = ""
    for char in arr[0], chaar in arr[1]:
        transposed += f"{char, chaar}"
    return transposed


print(transpose_two_strings(['Hello', 'World']))