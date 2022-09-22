from functools import reduce
def product_array(numbers):
    product_arr = []
    exclusion = 0
    for i in range(len(numbers)):
        copy_arr = numbers[:]
        del copy_arr[exclusion]
        product_arr.append(reduce(lambda total, next: total * next, copy_arr))
        exclusion += 1
    return product_arr


print(product_array([1, 2, 5]))
