def zero_plentiful(list):
    zero_count = 0
    sequence_count = 0
    no_change_seq = 0
    for num in list:
        if num == 0:
            zero_count += 1
            if zero_count >= 4:
                no_change_seq += 1
                sequence_count += 1
            elif zero_count < 4:
                sequence_count = 0
        else:
            zero_count = 0

    if no_change_seq > 0 and sequence_count < 1:
        return 0
    elif no_change_seq > 0 and sequence_count > 0:
        return no_change_seq
            


print(zero_plentiful([1, 2, 3, 0, 0, 0, 0, 1, 0, 2]))
print(zero_plentiful([0, 0, 0, 0, 2, 5, 4, 1, 0, 0, 0]))
print(zero_plentiful([8, 4, 2, 1, 0, 0, 0, 0, 4, 3, 1, 2]))
