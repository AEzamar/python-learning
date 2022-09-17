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


""" print(array_leader([1,2,3,4,0]))
print(array_leader([-36,-12,-27])) """


def array_leader1(numbers):
    return [num for num in numbers if num > sum(numbers[num:])]


def array_leader2(numbers):
    leaders = []
    for num in numbers:
        sub_lst = numbers[num:]
        print(numbers)
        if num > sum(sub_lst):
            leaders.append(num)
            print(numbers)
        if len(sub_lst) == 1 and num > 0:
            leaders.append(num)
        numbers.remove(num)
    return leaders


""" print(array_leader2([1,2,3,4,0]))
print(array_leader2([-36,-12,-27])) """


def array_leader3(numbers):
    leaders = []
    #print(numbers)
    while len(numbers):
        if numbers[0] > sum(numbers[1:]):
            leaders.append(numbers[0])
        del numbers[0]
        #print('Leaders 1:', leaders)
        """ if len(numbers) == 1 and sum(numbers) > 0:
            leaders.append(sum(numbers))
        print('Leaders 2:', leaders) """
    return leaders


print(array_leader3([1,2,3,4,0]))
print(array_leader3([-36,-12,-27]))
print(array_leader3([16, 17, 4, 3, 5, 2]))


def array_leader4(numbers):
    leaders = []
    #print(numbers)
    while len(numbers):
        if numbers[0] > sum(numbers[1:]):
            leaders.append(numbers[0])
        del numbers[0]
        #print('Leaders 1:', leaders)
        """ if len(numbers) == 1 and sum(numbers) > 0:
            leaders.append(sum(numbers))
        print('Leaders 2:', leaders) """
    return leaders


print(array_leader4([1,2,3,4,0]))
print(array_leader4([-36,-12,-27]))
print(array_leader4([16, 17, 4, 3, 5, 2]))