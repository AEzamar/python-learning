def contamination(text, char):
    contaminated = ""
    iteration = 0
    while iteration < len(text):
        contaminated += char
        iteration += 1
    return contaminated


print(contamination("hello", "]"))
print(contamination("Hey there", ">"))