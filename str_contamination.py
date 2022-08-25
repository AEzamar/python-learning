def contamination(txt, char):
    contaminated = ""
    iteration = 0
    while iteration < len(txt):
        contaminated += char
        iteration += 1
    return contaminated


print(contamination("hello", "]"))