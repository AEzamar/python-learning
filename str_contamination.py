def contamination(text, char):
    contaminated = ""
    i = 0
    while i < len(text):
        contaminated += char
        i += 1
    return contaminated


print(contamination("hello", "]"))
print(contamination("Hey there", ">"))