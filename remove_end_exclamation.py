import re
def remove(s):
    i = -1
    for char in s:
        if s[i] == '!':
            s.replace(s[i], "")
            i += -1

print(remove("!!!Hi!!!"))
print(-1 + -1)