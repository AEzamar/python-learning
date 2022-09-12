def to_csv_text(array):
    csv_st = ""
    for ele in array:
        csv_st += ','.join(map(str, ele)) + '\n'
    return csv_st.rstrip()  


print(to_csv_text([
    [ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]))


def to_csv_text1(list):
    csv_text = ""
    for sublist in list:
        csv_text += "".join(sublist)
    return csv_text


""" print(to_csv_text1([
    [ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]])) """