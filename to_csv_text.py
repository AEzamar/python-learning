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


#User submitted solution
""" def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array) """

