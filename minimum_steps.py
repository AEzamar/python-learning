def minimum_steps(numbers, value):
    total = 0
    steps = 0
    while total <= value:
        total += numbers[0] + numbers[1]
        del numbers[0]
        steps += 1
    return steps


print(minimum_steps([4,6,3], 7))