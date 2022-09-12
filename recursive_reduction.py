def digital_root(n):
    total = 0
    n_list = list(str(n))
    for digit in n_list[0]:
        total += int(digit)
    return total


print(digital_root(123456))