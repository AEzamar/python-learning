def transpose_two_strings(arr):
    transposed = ""
    """ for char in zip(arr[0], arr[1]):
        transposed += f"{str(char)}" + '\n' """
    len_diff = len(arr[0]) - len(arr[1])
    for i in range(len(arr[0]) + len_diff):
        transposed += f"{arr[0][i]} {arr[1][i]}\n" 
    return transposed.rstrip()


print(transpose_two_strings(['Hello', 'World']))

#[(title, year) for (title, year) in movies if year >= 2000]