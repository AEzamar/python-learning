def merge_arrays(first, second):
    merged_list = []
    for num in locals().values():
        merged_list.append(num)
    merged_list.sort()
    return merged_list


print(merge_arrays([3, 1, 1], [9, 6, 5]))
        