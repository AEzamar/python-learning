def print_array(arr):
    arr_st = ""
    for i in range(len(arr)):
        arr_st += str(arr[i]) + ','
    return arr_st


print(print_array([2, 4, 5, 2]))