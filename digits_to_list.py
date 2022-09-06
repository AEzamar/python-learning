def convert(item):
    return int(item)


def digitize(n):
    n_list = list(str(n))
    return n_list[::-1]


print(digitize(32514))