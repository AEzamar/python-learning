def print_array(arr):
    arr_st = ""
    for char in arr:
        arr_st += str(char) + ','
    return arr_st


print(print_array([2, 4, 5, 2]))