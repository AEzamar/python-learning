from codecs import unicode_escape_decode


numbers = [2, 3, 1, 3, 4, 2, 3, 6, 7, 5, 4, 8, 8, 9]
unique_list = []
for number in numbers:
    if number not in unique_list:
        unique_list.append(number)
        unique_list.sort()
print(unique_list)
