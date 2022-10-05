def sort_by_length(arr):
    arr.sort(key = lambda item: len(item))
    return arr


#User submitted solution
#I keep forgetting about sorted
""" def sort_by_length1(arr):
    return sorted(arr, key = len) """


print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))