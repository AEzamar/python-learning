import re
def remove(s):
    return re.sub('!$', "", s, 1)


print(remove("Dang!!!!!"))
print(remove('!hi! !hi!'))
print(remove('!Hi'))
print(remove('Hi'))
print(remove('!Hi!'))
print(remove('Hi!!'))
print(remove('Hi!'))
print(remove('!Hi! !Hi!'))

def remove1(s):
    for char in s:
        print(len(s))
        if s.index(char) == len(s) and char == '!':
            print('Char index', s.index(char))
            s.replace(char, "")
    return s

#print(remove1("Exclamation!!!"))


def remove2(s):
    if s[-1] == '!':
        return s[:-1]
    else: 
        return s


""" print(remove2('Exclamation!!!'))
print(remove2('!Hi! Hi!'))
print(remove2('Hi'))
print(remove2('!Hi')) """
