def arr_adder(arr):
    arr_st = ""
    for row in range(len(arr[0])):
        for col in range(len(arr)):
            arr_st += str(arr[col][row])
        arr_st += ' '
    return arr_st.lstrip()


print(arr_adder([
['J','L','L','M']
,['u','i','i','a']
,['s','v','f','n']
,['t','e','e','']]))

print(arr_adder([[ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
  [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
  [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
  [ '', 'o', '', '', 'e', '', '', 'l' ],
  [ '', 'c', '', '', 'r', '', '', '' ],
  [ '', 'h', '', '', 'h', '', '', '' ],
  [ '', 'o', '', '', 'o', '', '', '' ],
  [ '', 'n', '', '', 'u', '', '', '' ],
  [ '', 'd', '', '', 's', '', '', '' ],
  [ '', 'r', '', '', 'e', '', '', '' ],
  [ '', 'i', '', '', '', '', '', '' ],
  [ '', 'a', '', '', '', '', '', '' ]]))


#User submitted solutions
""" def arr_adder(arr):
    return ' '.join(map(''.join, zip(*arr))) """

#Another similar solution but without map
""" def arr_adder(arr): """
"""     return ' '.join(''.join(col) for col in zip(*arr)) """