def merge_arrays(first, second):
    merged_list = []
    for num in first and second:
        merged_list.append(num)
    merged_list.sort()
    return merged_list
        