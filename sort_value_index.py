def sort_by_value_and_index(lst):
    product_lst = [num * (i + 1) for i, num in enumerate(lst)]
    return product_lst
    #return [(num // i) for i, num in enumerate(product_lst)]
    #return product_lst



print(sort_by_value_and_index([23, 2, 3, 4, 5]))    