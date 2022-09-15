def sort_by_value_and_index(lst):
    i = 1
    product_lst = []
    for i in range(len(lst)):
        print(lst[i])
        product_lst.append(lst[i] * i + 1)
    return product_lst


print(sort_by_value_and_index([23, 2, 3, 4, 5]))    
