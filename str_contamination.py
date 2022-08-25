def contamination(txt, char):
    for ch in txt:
        contaminated = re.sub(ch, char, txt)
    return contaminated


print(contamination("hello", "*"))