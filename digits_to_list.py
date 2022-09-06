def digitize(n):
    n_list = list(str(n))
    n_list.sort()
    return n_list


print(digitize(32514))