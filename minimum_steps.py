def minimum_steps(numbers, value):
    total = 0
    steps = 0
    numbers.sort()
    while total < value:
        total += numbers[0] + numbers[1]
        del numbers[0]
        steps += 1
    return steps


print(minimum_steps([4,6,3], 7))
print(minimum_steps([10,9,9,8], 17))
print(minimum_steps([8,9,10,4,2], 23))