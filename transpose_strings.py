def transpose_two_strings(arr):
    transposed = ""
    #len_diff = len(arr[0]) - len(arr[1])
    """ for i in range(len(arr[0])):
        transposed += f"{arr[0][i]} {arr[1][i]}\n"  """
    #transposed += str([(char, chaar) for char in arr[0] for chaar in arr[1]])
    """ for char in zip(arr[0], arr[1]): """
    """     transposed += '\n' """
    """     transposed += f"{str(char)}" """
    main_len = 0
    main_len += len(arr[0]) if len(arr[0]) > len(arr[1]) else len(arr[1])
    #print(main_len)
    for i in range(main_len):
        transposed += f"{arr[0][i]}, {arr[1][i]}"
    return transposed.lstrip()


print(transpose_two_strings(['Hello', 'World']))
print(transpose_two_strings(['Hey', 'People']))
print(transpose_two_strings(['Tranpose', 'This']))