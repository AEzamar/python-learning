def product_array(numbers):
    product_arr = []
    exclusion = 0
    for i in range(len(numbers)):
        copy_arr = numbers[:]
        del numbers[exclusion]
                    
    return product_arr