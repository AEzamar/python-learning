def merge_arrays(arr1, arr2):
    merged_list = []
    for num in arr1 + arr2:
        if num not in merged_list:
            merged_list.append(num)
    merged_list.sort()
    return merged_list


print(merge_arrays([3, 1, 1], [9, 6, 5]))
        