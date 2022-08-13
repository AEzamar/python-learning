def emoji_converter(message):
    emoji_dty = {
        ":)": "😺",
        ":(": "☹️",
        ":D": "😃",
        "T_T": "😢"
    }
    emoji_str = " "
    word_list = message.split(' ')
    for word in word_list:
        emoji_str += emoji_dty.get(word, word) + " "
    return emoji_str


emoji_converter()