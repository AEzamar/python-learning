import re
def get_number_from_string(string):
    return re.match('\d+', string)
    

print(get_number_from_string("Hell1o Worl2d1"))