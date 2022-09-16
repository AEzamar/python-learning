from functools import reduce
def array_leader(numbers):
    leader = '0'
    for num in numbers:
        sub_arr = numbers[numbers.index(num):-1]
        if num > reduce(lambda total, next: total + next, sub_arr):
            leader = numbers[num] 
    return leader

print(array_leader([1,2,3,4,0]))