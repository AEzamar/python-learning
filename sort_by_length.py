def sort_by_length(arr):
    return arr.sort(key = lambda a: len(a))


print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))