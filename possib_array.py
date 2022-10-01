def is_all_possibilities(arr = []):
    arr.sort()
    for i in arr:
        print('i:', i, 'Arr[i]:', arr[i])
        if i == arr[i]:
            


print(is_all_possibilities([1, 3, 2, 0]))
print(is_all_possibilities([4, 2, 1, 0]))
