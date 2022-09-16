import functools
def array_leader(numbers):
    leader = numbers[0]
    for num in numbers:
        sub_arr = numbers[num:-1]
        if num > functools.reduce(sub_arr, lambda curr, next: curr + next):
            leader = numbers[num] 


print(array_leader([1,2,3,4,0]))