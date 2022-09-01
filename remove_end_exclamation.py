import re
def remove(s):
    return re.sub('!{1:}$', " ", s)


print(remove("!!!Hi!!!"))