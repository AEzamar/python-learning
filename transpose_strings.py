def transpose_two_strings(arr):
    transposed = ""
    """ for char in zip(arr[0], arr[1]):
        transposed += f"{str(char)}" + '\n' """
    #len_diff = len(arr[0]) - len(arr[1])
    """ for i in range(len(arr[0])):
        transposed += f"{arr[0][i]} {arr[1][i]}\n"  """
    #[(transposed += char, chaar) for (char, chaar) in arr[0], arr[1]]
    for char, chaar in zip(arr[0], arr[1]):
        print(char, chaar)
    return transposed.rstrip()


print(transpose_two_strings(['Hello', 'World']))
print(transpose_two_strings(["Hey", "People"]))

#[(title, year) for (title, year) in movies if year >= 2000]