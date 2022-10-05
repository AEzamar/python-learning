def sort_by_length(arr):
    return arr.sort(key = lambda item: len(item))


print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))