def transpose_two_strings(arr):
    transposed = ""
    for (char, ch) in arr[0], arr[1]:
        print(char)
        transposed += f"{char, ch}"
    return transposed.rstrip()


print(transpose_two_strings(['Hello', 'World']))