def to_csv_text(list):
    csv_text = ""
    for sublist in list:
        for ele in str(sublist) + ',' + '\n':
            csv_text += ele
    return csv_text    


print(to_csv_text([
    [ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] ))