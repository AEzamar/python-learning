def stringy(size):
    stringy_str = ""
    a = '1'
    b = '0'
    for i in range(size):
        if i % 2 == 0:
            stringy_str += a
        elif i % 3 == 0:
            stringy_str += b
    return stringy_str


print(stringy(4))