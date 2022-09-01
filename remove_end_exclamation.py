import re
def remove(s):
    mark_count = 0
    i = -1
    for char in s:
        if s[i] == '!':
            mark_count += 1
            re.sub('!$', "", s, mark_count)
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