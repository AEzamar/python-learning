def is_all_possibilities(arr = []):
    arr.sort()
    """ for i in range(len(arr)):
        print('i:', i, 'Arr[i]:', arr[i])
        if i != arr[i]:
            return False
        else:
            return True """


print(is_all_possibilities([1, 3, 2, 0]))
print(is_all_possibilities([4, 2, 1, 0]))
