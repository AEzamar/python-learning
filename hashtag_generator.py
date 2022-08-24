def hashtag_generator(str):
    str_list = str.lower().split()
    upper_str_list = []
    for stri in str_list:
        upper_str_list.append(stri[0].upper() + stri[1:])
        upper_str_list
    return f'#{"".join(upper_str_list)}'

print(hashtag_generator("This is a string"))
print(hashtag_generator("OOOH shit mang!"))