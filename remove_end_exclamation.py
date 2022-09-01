import re
def remove(s):
    i = -1
    for char in s:
        if s[i] == '!':
            s.replace('!$', "")
            i += -1
        elif s[i] != '!':
            return s


print(remove("!!!Hi!!!"))


def remove1(s):
    replaced_s = ""
    if s[:-1] == '!':
        replaced_s += s.replace('!', "")
    return replaced_s


print(remove1("!!!Hi!!!"))

#def remove1(s):
    #return s[:-1] s.replace(s[-1], "") 