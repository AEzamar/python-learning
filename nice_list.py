def is_nice(arr):
    nice_count = 0
    for num in arr:
        if num + 1 or num - 1 in arr:
            nice_count += 1
    return True if nice_count == len(arr) else False