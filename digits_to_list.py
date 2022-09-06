def digitize(n):
    n_list = str(n).split(" ")
    print(n_list)
    return n_list.sort()


print(digitize(32514))