import functools
def array_leader(lst):
    for num in lst:
        sub_arr = lst[num: -1]
        if num > functools.reduce(sub_arr, lambda curr, next: curr + next) 
