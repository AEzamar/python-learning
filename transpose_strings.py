def transpose_two_strings(arr):
    transposed = ""
    #len_diff = len(arr[0]) - len(arr[1])
    """ for i in range(len(arr[0])):
        transposed += f"{arr[0][i]} {arr[1][i]}\n"  """
    #transposed += str([(char, chaar) for char in arr[0] for chaar in arr[1]])
    """ for char in zip(arr[0], arr[1]): """
    """     transposed += '\n' """
    """     transposed += f"{str(char)}" """
    ran_len = 0
    ran_len += len(arr[0]) if len(arr[0]) > len(arr[1]) else ran_len += len(arr[1])
    print(ran_len)
    for i in range(len(arr[0]) > len(arr[1]) or len(arr[1]) > len(arr[0])):
        print(arr[0][i])
    return transposed.lstrip()


print(transpose_two_strings(['Hello', 'World']))
print(transpose_two_strings(["Hey", "People"]))