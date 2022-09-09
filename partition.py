def partition(arr, classifier_method):
    list_a = []
    list_b = []
    for ele in arr:
        list_a.append(ele) if classifier_method(ele) else list_b.append(ele)
    return list_a, list_b


print(partition(['dog', 'cat', 'moose', 'duck', 'goose', 'ferret', 'cow'], lambda x: len(x) == 3))


#User submitted solution, very nice use of filter
""" from itertools import filterfalse
def partition(lis, classifier_method):
    fir = list(filter(classifier_method, lis))
    sec = list(filterfalse(classifier_method, lis))
    return (fir, sec) """