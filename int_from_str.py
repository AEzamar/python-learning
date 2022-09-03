import re
def get_number_from_string(string):
    nums = ""
    ints_str = '0123456789'
    for char in string:
        if char in ints_str:
            nums += char
    return int(nums)


print(get_number_from_string("Hell1o Worl2d1"))

def get_number_from_string1(string):
    nums = re.search('[0-9]', string)
    return nums.group()


print(get_number_from_string1("He2llo1 Wo1r1ld2"))

#CD solutions
""" def get_number_from_string(s):
    return int(re.sub(r'\D', '', s)) """
#Also found this one that uses filter and isdigit()
""" def get_number_from_string(s):
    return int(filter(str.isdigit, s)) """
