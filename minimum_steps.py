from functools import reduce
def minimum_steps(numbers, value):
    total = 0
    steps = 0
    unique_numbers = list(set(numbers))
    numbers.sort()
    print(numbers)
    """ for i in range(len(numbers)):
        steps += 1
        total += numbers[i] + numbers[i + 1]
        del numbers[0]
        if total > value:
            break """

    while total < value:
        steps += 1
        total += numbers[0] + numbers[1]
        del numbers[0], numbers[1]
        if len(numbers) == 1:
            total += numbers[0]
        print(numbers)
        print(total)
    return steps


print(minimum_steps([4,6,3], 7))
print(minimum_steps([10,9,9,8], 17))
print(minimum_steps([8,9,10,4,2], 23))
print(minimum_steps([19,98,69,28,75,45,17,98,67], 464))