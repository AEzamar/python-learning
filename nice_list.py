def is_nice(arr):
    nice_count = 0
    for num in arr:
        if num + 1 in arr:
            nice_count += 1
        elif num - 1 in arr:
            nice_count += 1
        else:
            return False
    return True if nice_count == len(arr) else False


""" print(is_nice([2, 10, 9, 3]))
print(is_nice([4, 2, 1])) """


def is_nice1(arr):
    nice_arr = []
    nice_arr += [num for num in arr if num + 1 in arr]
    nice_arr += [num for num in arr if num - 1 in arr]
    return True if len(nice_arr) == len(arr) else False
    

""" print(is_nice1([4, 2, 1]))
print(is_nice1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(is_nice1([2, 10, 9, 3])) """


def is_nice2(arr):
    arr_copy = arr[:]
    filtered_arr = filter(lambda num: num + 1 in arr, arr_copy)
    return list(filtered_arr)


print(is_nice2([4, 2, 1]))