def sort_by_value_and_index(lst):
    i = 1
    product_lst = []
    for ele in lst:
        product_lst.append((ele * i))
        i += 1
        product_lst.sort()
    return [num // (product_lst.index(num) + 1) for num in product_lst]
    #return product_lst



print(sort_by_value_and_index([23, 2, 3, 4, 5]))    
