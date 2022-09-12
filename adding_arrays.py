def arr_adder(arr):
    arr_st = ""
    col = 0
    for row in arr:
        print(row)
        for col in row:
            arr_st += str(arr[row][col])
    return arr_st


print(arr_adder([
['J','L','L','M']
,['u','i','i','a']
,['s','v','f','n']
,['t','e','e','']]))