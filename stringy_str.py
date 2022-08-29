def stringy(size):
    stringy_str = ""
    a = '1'
    b = '0'
    for i in range(size):
        stringy_str += a or b
    return stringy_str


print(stringy(4))