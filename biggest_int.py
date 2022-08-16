def max_int(list):
    biggest = list[0]
    for num in list:
        if num > biggest:
            biggest = num
    return biggest