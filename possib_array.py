def is_all_possibilities(arr = []):
    arr.sort()
    for i in arr:
        if i == arr[i]:
            return True
        elif i != arr[i]:
            return False


print(is_all_possibilities([1, 3, 2, 0]))
print(is_all_possibilities([4, 2, 1, 0]))
