def clean_capitalize(str_list):
    clean_str_list = []
    for str in str_list:
        low_str = str.lower() + str[0].upper() + str[1:]
        clean_str_list.append(low_str)
    print(clean_str_list)


word_list = ['HeLlO', 'dANg', "sHHieet", "CRAP", "manG", "MenG"]
clean_capitalize(word_list)