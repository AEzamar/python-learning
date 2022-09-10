def print_array(arr):
    arr_st = str(arr)[1:-1]
    return arr_st.replace("\s+", "")

print(print_array([2, 4, 5, 2]))