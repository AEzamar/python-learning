def digitize(n):
    n_list = str(n).split(" ")
    print(n_list.sort(reverse=True))
    return n_list


print(digitize(32514))