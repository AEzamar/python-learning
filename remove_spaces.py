import re
def no_space(x):
    return re.sub('\s', "", x)


#Solution from anoter developer
""" def no_space(x):
    return x.replace("", "") """