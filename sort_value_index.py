import math


#sort_by_product = lambda i, ele: ele * (i + 1)
def sort_by_value_and_index(lst):
    product_lst = [num * (i + 1) for i, num in enumerate(lst)]
    print(product_lst)
    product_lst.sort()
    return [num // (i + 1) for i, num in enumerate(product_lst)]
    #return product_lst


print(sort_by_value_and_index([23, 2, 3, 4, 5]))


""" print(math.sqrt(4))
print(math.sqrt(9))
print(math.sqrt(23)) """


def sort_by_value_and_index1(lst):
    return [ele * (i + 1) for (i, ele) in enumerate(lst)]


#print(sort_by_value_and_index1([23, 2, 3, 4, 5]))
