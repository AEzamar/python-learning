def emoji_converter():
    feeling = input("How are you feeling today? ")
    emoji_dty = {
        ":)": "😺",
        ":(": "☹️",
        ":D": "😃",
        "T_T": "😢"
    }
    emoji_str = " "
    word_list = feeling.split(' ')
    for word in word_list:
        emoji_str += emoji_dty.get(word, word) + " "
    print(emoji_str)


emoji_converter()