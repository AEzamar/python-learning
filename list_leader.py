#from functools import reduce
def array_leader(numbers):
    leaders = []
    for num in numbers:
        sub_arr = numbers[num:]
        """ print(sub_arr)
        print(sum(sub_arr)) """
        if num > sum(sub_arr):
            leaders.append(num)
        elif len(sub_arr) == 1 and sum(sub_arr) > 0:
            leaders.append(sum(sub_arr))
    return leaders


print(array_leader([1,2,3,4,0]))
print(array_leader([-36,-12,-27]))


def array_leader1(numbers):
    return [num for num in numbers if num > sum(numbers[num:])]

def array_leader2(numbers):
    leaders = []
    for num in numbers:
        sub_lst = numbers[num:]
        if num > sum(sub_lst):
            leaders.append(num)
            numbers.remove(num)
        if len(sub_lst) == 1 and sum(sub_lst) > 0:
            leaders.append(sum(sub_lst))
    return leaders


print(array_leader2([1,2,3,4,0]))
print(array_leader2([-36,-12,-27]))