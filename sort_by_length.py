def sort_by_length(arr):
    return arr.sort(key = lambda a, b: len(a) - len(b))


print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))