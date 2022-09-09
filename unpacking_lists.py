letters = ["a", "b", "c"]
#The enumerate method allows us to iterate and get then index of the items
#on a list
#It is also possible to unpack while declaring variables in a for loop
for index, letter in enumerate(letters):
    print(f"{index}: {letter}")