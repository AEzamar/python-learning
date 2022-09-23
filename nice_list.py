def is_nice(arr):
    nice_count = 0
    nice_bool = False
    for num in arr:
        if num + 1 in arr:
            nice_count += 1
        elif num - 1 in arr:
            nice_count += 1
    return nice_bool = True if nice_count == len(arr) else nice_bool = False


print(is_nice([2, 10, 9, 3]))
print(is_nice([4, 2, 1]))