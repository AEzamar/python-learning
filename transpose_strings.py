def transpose_two_strings(arr):
    transposed = ""
    string_zip = dict(zip(arr[0], arr[1]))
    for key, value in string_zip.items():
        transposed += str(f"{key} {value}")
        transposed += '\n'
    return transposed.rstrip()


#print(transpose_two_strings(['Hello', 'World']))
print(transpose_two_strings(['Hey', 'People']))
#print(transpose_two_strings(['Tranpose', 'This']))