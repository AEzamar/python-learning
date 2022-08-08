numbers = [4, 20, 69, 69.5, 33, 44, 11, 12, 21]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print(biggest)