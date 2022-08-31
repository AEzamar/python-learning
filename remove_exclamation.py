import re
def remove(s):
    return re.sub('!', "", s)


#print(remove("Dang!!!!!"))


def remove1(s):
    for char in s:
        print(len(s))
        if s.index(char) == len(s) and char == '!':
            print('Char index', s.index(char))
            s.replace(char, "")
    return s

print(remove1("Exclamation!!!"))