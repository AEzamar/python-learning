def convert(item):
    return int(item)


def digitize(n):
    n_list = list(str(n))
    digitized_list = [int(num) for num in n_list]
    return digitized_list[::-1]


print(digitize(32514))

#Other coder's solution, there's map in python btw
""" def digitize(n):
    return map(int, str(n)[::-1]) """