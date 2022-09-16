#from functools import reduce
def array_leader(numbers):
    leaders = []
    for num in numbers:
        sub_arr = numbers[num:]
        """ print(sub_arr)
        print(sum(sub_arr)) """
        if num > sum(sub_arr):
            leaders.append(num) 
    return leaders


print(array_leader([1,2,3,4,0]))
print(array_leader([1, 2]))


def array_leader1(numbers):
    return [num for num in numbers if num > sum(numbers[num:])]