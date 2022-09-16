#from functools import reduce
def array_leader(numbers):
    leader = 0
    for num in numbers:
        sub_arr = numbers[num:]
        """ print(sub_arr)
        print(sum(sub_arr)) """
        if num > sum(sub_arr):
            leader = num 
    return leader


print(array_leader([1,2,3,4,0]))


def array_leader1(numbers):
    return [num for num in numbers if num > sum(numbers[num:])]