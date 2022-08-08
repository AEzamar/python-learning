numbers = [4, 20, 69, 69.5, 33, 44, 11, 12, 21]
biggest_int = numbers[0]
for num in numbers:
    if num > biggest_int:
        biggest_int = num
print(biggest_int)