def is_nice(arr):
    nice_count = 0
    for num in arr:
        if num + 1 in arr:
            nice_count += 1
        elif num - 1 in arr:
            nice_count += 1
        
    return True if nice_count == len(arr) else False


print(is_nice([2, 10, 9, 3]))
print(is_nice([4, 2, 1]))


def is_nice1(arr):
    nice_arr = [num for num in arr if num + 1 in arr]
    print(nice_arr)
    if len == len(arr):
        return True
    else:
        return False


print(is_nice1([4, 2, 1]))
