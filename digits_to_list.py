def convert(item):
    return int(item)


def digitize(n):
    n_list = list(str(n))
    [int(num) for num in n_list]
    return n_list[::-1]


print(digitize(32514))