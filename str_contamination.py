def contamination(txt, char):
    for ch in txt:
        contaminated = txt.replace(f"\{ch}\g", char)
    return contaminated


print(contamination("hello", "*"))