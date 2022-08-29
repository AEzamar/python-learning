import re
def string_clean(s):
    return re.str.replace(/{0-9}/g, " ")


print(string_clean("Ohh12 dang112 mang"))