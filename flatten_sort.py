def flatten_and_sort(array):
    flat_arr = []
    i = 0
    for j in range(len(array)):
        flat_arr += f"{array[i][j]}"
        i += 1
    return flat_arr

print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))