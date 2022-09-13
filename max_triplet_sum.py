def max_tri_sum(numbers):
    uq_list = []
    """ for num in numbers:
        if num not in uq_list:
            uq_list.append(num) """
    [uq_list.append(num) for num in numbers if num not in uq_list]
    uq_list.sort(reverse=True)
    
    return uq_list[0] + uq_list[1] + uq_list[2]


print(max_tri_sum([3,2,6,8,2,3]))