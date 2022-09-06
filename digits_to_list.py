def digitize(n):
    n_list = str(n).split()
    new_list = []
    while len(n_list):
        new_list.append(n_list.pop())
    return new_list


print(digitize(32514))