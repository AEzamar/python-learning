def convert(item):
    return int(item)


def digitize(n):
    n_list = list(str(n))
    return [num for num in n_list]


print(digitize(32514))