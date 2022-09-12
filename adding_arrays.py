def arr_adder(arr):
    arr_st = ""
    for row in range(len(arr)):
        arr_st += ' '
        for col in range(len(arr[0])):
            arr_st += str(arr[col][row])
    return arr_st.lstrip()


print(arr_adder([
['J','L','L','M']
,['u','i','i','a']
,['s','v','f','n']
,['t','e','e','']]))