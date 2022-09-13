def multiply_all(list):
    list_copy = list[:]
    def multiplier(int):
        return [num * int for num in list_copy]


print(multiply_all([1, 2, 3]))