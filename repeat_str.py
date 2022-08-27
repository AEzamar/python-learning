def repeat_str(repeat, string):
    repeated = ""
    for iteration in range(repeat):
        repeated += string
    return repeated


print(repeat_str(3, "Hi"))