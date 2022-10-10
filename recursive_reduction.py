def digital_root(n):
    total = 0
    n_list = list(map(int, list(str(n))))
    print(n_list)
    for digit in range(len(n_list)):
        total += sum(int(digit))
    return total


print(digital_root(123456))