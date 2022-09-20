def transpose_two_strings(arr):
    transposed = ""
    """ main_len = 0
    main_len += len(arr[0]) if len(arr[0]) > len(arr[1]) else len(arr[1])
    for i in range(main_len):
        transposed += '\n'
        transposed += f"{arr[0][i]} {arr[1][i]}" """
    for char in zip(arr[0], arr[1]):
        transposed += '\n'
        transposed += str(char)
    return transposed.lstrip()


print(transpose_two_strings(['Hello', 'World']))
print(transpose_two_strings(['Hey', 'People']))
#print(transpose_two_strings(['Tranpose', 'This']))