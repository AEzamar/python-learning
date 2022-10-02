from functools import reduce
def minimum_steps(numbers, value):
    total = 0
    steps = 0
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    #print(numbers)
    while total < value:
        total += numbers_copy[0]
        del numbers_copy[0]
        #print(numbers_copy)
        steps += 1
        #print(total)
    return steps


print(minimum_steps([4,6,3], 7))
print(minimum_steps([10,9,9,8], 17))
print(minimum_steps([8,9,10,4,2], 23))
print(minimum_steps([19,98,69,28,75,45,17,98,67], 464))