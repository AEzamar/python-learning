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
    if s[-1] == '!':
        return s[:-1]
    else: 
        return s


""" print(remove1('Exclamation!!!'))
print(remove1('!Hi! Hi!'))
print(remove1('Hi'))
print(remove1('!Hi')) """

#CW solution, very elegant
#def remove(s):
    #return s[:-1] if s.endswith('!') else s