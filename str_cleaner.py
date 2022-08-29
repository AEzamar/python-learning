import re
def string_clean(s):
    return re.sub("[0-9]", "", s)


print(string_clean("Ohh12 dang112 mang"))
print(string_clean("412For It4523 May9434 Seem3123, Life92323 Is313 Nothing563, But1312 A31 Dream98 Within9842 A12 Dream633123"))