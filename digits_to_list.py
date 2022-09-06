def digitize(n):
    return (str(n).split()).sort(reverse=True)


print(digitize(32514))