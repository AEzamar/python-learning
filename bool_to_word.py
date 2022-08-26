def bool_to_word(boolean):
    if boolean ==  True:
        boolean = "Yes"
    else:
        boolean = "No"
    return boolean


print(bool_to_word(True))
print(bool_to_word(False))