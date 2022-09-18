#from functools import reduce
def array_leader1(numbers):
    leaders = []
    for num in numbers:
        sub_arr = numbers[num:]
        print(sub_arr)
        print(sum(sub_arr))
        if num > sum(sub_arr):
            leaders.append(num)
        elif len(sub_arr) == 1 and sum(sub_arr) > 0:
            leaders.append(sum(sub_arr))
    return leaders


def array_leader11(numbers):
    return [num for num in numbers if num > sum(numbers[num:])]


def array_leader12(numbers):
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


def array_leader13(numbers):
    leaders = []
    #print(numbers)
    while len(numbers):
        if numbers[0] > sum(numbers[1:]):
            leaders.append(numbers[0])
        del numbers[0]
        #print('Leaders 1:', leaders)
        if len(numbers) == 1 and sum(numbers) > 0:
            leaders.append(sum(numbers))
        print('Leaders 2:', leaders)
    return leaders


def array_leader(numbers):
    leaders = []
    while len(numbers):
        if numbers[0] > sum(numbers[1:]):
            leaders.append(numbers[0])
        del numbers[0]
    return leaders


print(array_leader([1,2,3,4,0]))
print(array_leader([-36,-12,-27]))
print(array_leader([16, 17, 4, 3, 5, 2]))


#User submitted solution
""" def array_leaders(numbers):
    return [n for (i,n) in enumerate(numbers) if n>sum(numbers[(i+1):])] """