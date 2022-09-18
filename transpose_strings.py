def transpose_two_strings(arr):
    transposed = ""
    for char, ch in (arr[0], arr[1]):
        transposed += f"{char} {ch}\n"
    return transposed.rstrip()


print(transpose_two_strings(['Hello', 'World']))