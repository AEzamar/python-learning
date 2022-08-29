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

def stringy1(size):
    str_list = []
    a = '1'
    b = '0'
    for i in range(size):
        str_list.append(a)
    for it in range(size):
        str_list.append(b)
    return "".join(str_list)


print(stringy1(4))