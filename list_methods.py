numbers = [2, 5, 1, 3, 9, 69, 4, 7, 8, 10]
numbers2 = numbers.copy()
numbers.append(22)
numbers.insert(6, 33)
numbers.remove(69)
numbers.sort()
print(numbers)
print(f"Numbers copy: {numbers2}")