from functools import reduce
def product_array(numbers):
    product_arr = []
    for i in range(len(numbers)):
        copy_arr = numbers[:]
        del copy_arr[i]
        product_arr.append(reduce(lambda total, next: total * next, copy_arr))
    return product_arr


print(product_array([1, 2, 5]))
print(product_array([3, 27, 4, 2]))
print(product_array([13,10,5,2,9]))


#User submitted solution
""" from operator import mul
from functools import reduce

def product_array(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers] """

#This solution is even better holy molly
""" from numpy import prod
def product_array(numbers):
    p = prod(numbers)
    return [p // i for i in numbers] """