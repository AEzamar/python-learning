def is_all_possibilities(arr = []):
    return filter(lambda i , item: item == i, enumerate(arr))
    arr.sort()
    possib_count = 0
    for i in range(len(arr)):
        if i == arr[i]:
            possib_count += 1
    return True if possib_count == len(arr) else False


print(is_all_possibilities([1, 3, 2, 0]))
print(is_all_possibilities([0, 2, 1, 3]))
print(is_all_possibilities([4, 2, 1, 0]))
