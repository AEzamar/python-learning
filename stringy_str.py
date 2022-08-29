def stringy(size):
    stringy_str = ""
    binary_tuple = ('1', '0')
    a, b = binary_tuple
    for i in range(size):
        stringy_str += a
        stringy_str += b
    return stringy_str


print(stringy(4))