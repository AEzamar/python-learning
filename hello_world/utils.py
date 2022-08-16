def find_max(list):
    max_int = list[0]
    for num in list:
        if num > max_int:
            max_int = num
    return max_int