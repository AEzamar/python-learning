def transpose_two_strings(arr):
    transposed = ""
    """ main_len = 0
    main_len += len(arr[0]) if len(arr[0]) > len(arr[1]) else len(arr[1])
    for i in range(main_len):
        transposed += '\n'
        transposed += f"{arr[0][i]} {arr[1][i]}"
        if arr[0][i] or arr[1][i] == None:
            transposed += " " """
    string_zip = dict(zip(arr[0], arr[1]))
    for key, value in string_zip.items():
        transposed += str(f"{key} {value}")
        transposed += '\n'
    return transposed.rstrip()


#print(transpose_two_strings(['Hello', 'World']))
print(transpose_two_strings(['Hey', 'People']))
#print(transpose_two_strings(['Tranpose', 'This']))