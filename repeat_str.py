def repeat_str(repeat, string):
    repeated = ""
    for iteration in range(repeat):
        repeated += string
    return repeated


print(repeat_str(3, "Hi"))
print(repeat_str(5, "Oi!"))
print(repeat_str(6, "Oh yeah"))