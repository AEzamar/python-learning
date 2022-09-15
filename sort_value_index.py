def sort_by_value_and_index(lst):
    i = 1
    product_lst = []
    for ele in lst:
        product_lst.append((ele * i))
        i += 1
    return product_lst


print(sort_by_value_and_index([23, 2, 3, 4, 5]))    
