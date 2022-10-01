def is_all_possibilities(arr = []):
    arr.sort()
    for i in arr:
        if arr[i] == i:
            return True
        else:
            return False


print(is_all_possibilities([1, 3, 2, 0]))
print()
