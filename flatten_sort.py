def flatten_and_sort(array):
    flat_arr = []
    for num in array:
        flat_arr += num  
    flat_arr.sort()
    return flat_arr

print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))


#User submitted solution
""" from itertools import chain
def flatten_and_sort(array):
    return sorted((chain(*array))) """