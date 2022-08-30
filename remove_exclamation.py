import re
def remove(s):
    return re.sub('!', "", s)


print(remove("Dang!!!!!"))


def remove1(s):
    for char in s:
        if s.index(char) == len(s) and char == '!':
            s.replace(char, "")
    return s