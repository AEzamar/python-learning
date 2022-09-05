def to_csv_text(list):
    csv_text = ""
    i = 0
    for ele in list:
        csv_text += str(",".join(ele[i]))
        i += 1
    return csv_text    


print(to_csv_text([
    [ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] ))