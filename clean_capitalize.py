def clean_capitalize(str_list):
    clean_str_list = []
    for str in str_list:
        low_str = str.lower()
        up_str = low_str[0].upper() + low_str[1:]
        clean_str_list.append(up_str)
    print(clean_str_list)


word_list = ['HeLlO', 'dANg', "sHHieet", "CRAP", "manG", "MenG"]
clean_capitalize(word_list)