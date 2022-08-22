def zero_plentiful(list):
    zero_count = 0
    for num in list:
        no_change_seq = 0
        if num == 0:
            zero_count += 1
            if zero_count == 4:
                no_change_seq += 1
        else:
            zero_count = 0

    if no_change_seq > 0:
        return no_change_seq
    else:
        return 0


print(zero_plentiful([1, 2, 3, 0, 0, 0, 1, 0, 2]))
