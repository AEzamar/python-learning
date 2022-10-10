def to_float_array(arr):
    return list(map(float or int, arr))


print(to_float_array(["1.1", "2.2", "3.3"]))
print(to_float_array([1, 2, 3]))