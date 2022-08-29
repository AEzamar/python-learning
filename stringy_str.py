def stringy(size):
    stringy_str = ""
    a = '1'
    b = '0'
    for i in range(1, size):
        print('iteration', i)
        if i % 2 == 0:
            print('i % 2', i)
            stringy_str += a
        elif i % 3 == 0:
            print('i % 3', i)
            stringy_str += b
    return stringy_str


print(stringy(4))