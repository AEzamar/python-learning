import re
def remove(s):
    i = -1
    for char in s:
        if s[i] == '!':
            s.replace(s[i], "")
            i += -1
        elif s[i] != '!':
            return s

print(remove("!!!Hi!!!"))
print(-1 + -1)

def remove1(s):
    return s[:-1] if '!' in s 