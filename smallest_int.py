def find_smallest_int(arr):
    return min(arr)


def find_smallest_int1(arr):
    smallest = 0
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest