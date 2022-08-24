def hashtag_generator(str):
    str_list = str.split()
    upper_str_list = []
    for stri in str_list:
        upper_str_list.append(stri[0].upper() + stri[1:])
    return f"#{upper_str_list.join()}"

print(hashtag_generator("This is a string"))