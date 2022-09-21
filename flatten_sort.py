def flatten_and_sort(array):
    """ flat_arr = []
    for i in range(len(array)):
        flat_arr += array[i] """
    flat_arr = []
    [flat_arr.append(num) for num in array]   
    flat_arr.sort()
    return flat_arr

print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))