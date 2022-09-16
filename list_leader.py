#from functools import reduce
def array_leader(numbers):
    leader = 0
    for num in numbers:
        sub_arr = numbers[numbers.index(num):]
        print(sub_arr)
        if num > sum(sub_arr):
            leader = num 
    return leader

print(array_leader([1,2,3,4,0]))