def arr(n = 0):
    return [] if n < 1 else list(range(n))


print(arr(5))
print(arr())
print(arr(10))