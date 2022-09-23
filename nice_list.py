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