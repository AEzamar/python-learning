numbers = [5, 2, 5, 2, 2]
numbers1 = [1, 1, 1, 1, 5]
for num in numbers1:
    str = ""
    for n in range(num + 1):
        str += "x"
    print(str)
